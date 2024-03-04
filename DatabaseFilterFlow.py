from graphviz import Digraph

dot = Digraph(comment='Database Selection Process')

# Define styles for different kinds of nodes
start_style = {'shape': 'ellipse', 'style': 'filled', 'color': 'lightblue'}
decision_style = {'style': 'filled', 'fillcolor': '#B2EBF2'}
final_style = {'shape': 'doubleoctagon', 'style': 'filled', 'fillcolor': '#FFD966'}
exclude_style = {'shape': 'rectangle', 'style': 'filled', 'fillcolor': '#FFCDD2'}

# Add nodes
dot.node('Start', 'Start\n1000 Databases', **start_style)
dot.node('ChemData', 'Contains Chemical Data?\n800 left', **decision_style)
dot.node('RegularUpdate', 'Regularly Updated?\n700 left', **decision_style)
dot.node('KeywordSearch', 'Supports Keyword Search?\n600 left', **decision_style)
dot.node('PublicAccess', 'Publicly Accessible?\n500 left', **decision_style)
dot.node('EasyPermission', 'Easy Permission?\n400 left', **decision_style)
dot.node('VerifiedData', 'Data Verified?\n300 left', **decision_style)
dot.node('WideCoverage', 'Wide PDE Coverage?\n250 left', **decision_style)
dot.node('PositiveFeedback', 'Positive Feedback?\n245 left', **decision_style)
dot.node('Final', 'Final Selection\n245 Databases', **final_style)

# Add exclude nodes
dot.node('Ex1', 'Exclude: No Chemical Data', **exclude_style)
dot.node('Ex2', 'Exclude: Not Regularly Updated', **exclude_style)
dot.node('Ex3', 'Exclude: No Keyword Search', **exclude_style)
dot.node('Ex4', 'Exclude: Not Publicly Accessible', **exclude_style)
dot.node('Ex5', 'Exclude: Difficult Permission', **exclude_style)
dot.node('Ex6', 'Exclude: Data Not Verified', **exclude_style)
dot.node('Ex7', 'Exclude: Limited PDE Coverage', **exclude_style)
dot.node('Ex8', 'Exclude: Negative Feedback', **exclude_style)

# Add edges for main path
dot.edges([('Start', 'ChemData'), ('ChemData', 'RegularUpdate'), ('RegularUpdate', 'KeywordSearch'),
           ('KeywordSearch', 'PublicAccess'), ('PublicAccess', 'EasyPermission'), 
           ('EasyPermission', 'VerifiedData'), ('VerifiedData', 'WideCoverage'), 
           ('WideCoverage', 'PositiveFeedback'), ('PositiveFeedback', 'Final')])

# Add edges for exclude paths
dot.edge('ChemData', 'Ex1', color='red')
dot.edge('RegularUpdate', 'Ex2', color='red')
dot.edge('KeywordSearch', 'Ex3', color='red')
dot.edge('PublicAccess', 'Ex4', color='red')
dot.edge('EasyPermission', 'Ex5', color='red')
dot.edge('VerifiedData', 'Ex6', color='red')
dot.edge('WideCoverage', 'Ex7', color='red')
dot.edge('PositiveFeedback', 'Ex8', color='red')

# Generate and view the graph
dot.render('complex_database_selection_tree', view=True, format='png')
