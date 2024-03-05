from graphviz import Digraph

dot = Digraph(comment='Database Selection Process')

# Define styles for different kinds of nodes
start_style = {'shape': 'ellipse', 'style': 'filled', 'fillcolor': '#4CAF50'}
decision_style = {'shape': 'diamond', 'style': 'filled', 'fillcolor': '#B2EBF2'} 
final_style = {'shape': 'doubleoctagon', 'style': 'filled', 'fillcolor': '#FFD966'}
exclude_style = {'shape': 'rect', 'style': 'filled', 'fillcolor': '#FFCDD2'}

# Add nodes
dot.node('Start', 'Start\n1000', **start_style)
dot.node('ChemData', 'Chemical\nData?\n800', **decision_style)
dot.node('Format', 'Standard\nFormat?\n750', **decision_style)
dot.node('Update', 'Regular\nUpdates?\n700', **decision_style)  
dot.node('API', 'API?\n650', **decision_style)
dot.node('Search', 'Keyword\nSearch?\n600', **decision_style)
dot.node('Public', 'Publicly\nAccessible?\n500', **decision_style)
dot.node('Permission', 'Easy\nPermission?\n400', **decision_style)
dot.node('Verified', 'Data\nVerified?\n300', **decision_style)
dot.node('Coverage', 'Wide PDE\nCoverage?\n250', **decision_style)  
dot.node('Feedback', 'Positive\nFeedback?\n245', **decision_style)
dot.node('Final', 'Final\nSelection\n245', **final_style)

# Add exclude nodes  
dot.node('Ex1', 'No\nChemical Data', **exclude_style)
dot.node('Ex2', 'Non-Standard\nFormat', **exclude_style)  
dot.node('Ex3', 'Not Regularly\nUpdated', **exclude_style)
dot.node('Ex4', 'No API', **exclude_style)
dot.node('Ex5', 'No Keyword\nSearch', **exclude_style)  
dot.node('Ex6', 'Not Publicly\nAccessible', **exclude_style)
dot.node('Ex7', 'Difficult\nPermission', **exclude_style)
dot.node('Ex8', 'Data Not\nVerified', **exclude_style)
dot.node('Ex9', 'Limited PDE\nCoverage', **exclude_style)
dot.node('Ex10', 'Negative\nFeedback', **exclude_style)

# Add edges for main path
dot.edge('Start', 'ChemData', color='darkgreen')
dot.edge('ChemData', 'Format', color='darkgreen')
dot.edge('Format', 'Update', color='darkgreen')
dot.edge('Update', 'API', color='darkgreen')
dot.edge('API', 'Search', color='darkgreen')
dot.edge('Search', 'Public', color='darkgreen')
dot.edge('Public', 'Permission', color='darkgreen')
dot.edge('Permission', 'Verified', color='darkgreen')
dot.edge('Verified', 'Coverage', color='darkgreen')
dot.edge('Coverage', 'Feedback', color='darkgreen')
dot.edge('Feedback', 'Final', color='darkgreen')

# Add edges for exclude paths
dot.edge('ChemData', 'Ex1', color='red')  
dot.edge('Format', 'Ex2', color='red')
dot.edge('Update', 'Ex3', color='red')
dot.edge('API', 'Ex4', color='red')  
dot.edge('Search', 'Ex5', color='red')
dot.edge('Public', 'Ex6', color='red')
dot.edge('Permission', 'Ex7', color='red')
dot.edge('Verified', 'Ex8', color='red') 
dot.edge('Coverage', 'Ex9', color='red')
dot.edge('Feedback', 'Ex10', color='red')

# Set layout to neato for a circular layout
dot.graph_attr['layout'] = 'neato'
# Increase node separation
dot.graph_attr['nodesep'] = '0.5'
dot.graph_attr['ranksep'] = '1.5'

# Generate and view the graph
dot.render('circular_database_selection', view=True, format='png')
