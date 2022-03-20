from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.happiness_db

# Drops collection if available to remove duplicates
db.happiness.drop()

# Creates a collection in the database and inserts two documents
db.happiness.insert_many(
    [
        {'rank': '1', 'Country':'Finland', 'Score': '7.769', 'GDP': '1.34', 'social_support':'1.587', 'freedom':'0.596', 'life_expectancy': '81.9'},
{'rank': '2', 'Country':'Denmark', 'Score': '7.6', 'GDP': '1.383', 'social_support':'1.573', 'freedom':'0.592', 'life_expectancy': '80.9'},
{'rank': '3', 'Country':'Norway', 'Score': '7.554', 'GDP': '1.488', 'social_support':'1.582', 'freedom':'0.603', 'life_expectancy': '82.4'},
{'rank': '4', 'Country':'Iceland', 'Score': '7.494', 'GDP': '1.38', 'social_support':'1.624', 'freedom':'0.591', 'life_expectancy': '83'},
{'rank': '5', 'Country':'Netherlands', 'Score': '7.488', 'GDP': '1.396', 'social_support':'1.522', 'freedom':'0.557', 'life_expectancy': '82.3'},
{'rank': '6', 'Country':'Switzerland', 'Score': '7.48', 'GDP': '1.452', 'social_support':'1.526', 'freedom':'0.572', 'life_expectancy': '83.8'},
{'rank': '7', 'Country':'Sweden', 'Score': '7.343', 'GDP': '1.387', 'social_support':'1.487', 'freedom':'0.574', 'life_expectancy': '82.8'},
{'rank': '8', 'Country':'New Zealand', 'Score': '7.307', 'GDP': '1.303', 'social_support':'1.557', 'freedom':'0.585', 'life_expectancy': '82.3'},
{'rank': '9', 'Country':'Canada', 'Score': '7.278', 'GDP': '1.365', 'social_support':'1.505', 'freedom':'0.584', 'life_expectancy': '82.4'},
{'rank': '10', 'Country':'Austria', 'Score': '7.246', 'GDP': '1.376', 'social_support':'1.475', 'freedom':'0.532', 'life_expectancy': '81.5'},
{'rank': '11', 'Country':'Australia', 'Score': '7.228', 'GDP': '1.372', 'social_support':'1.548', 'freedom':'0.557', 'life_expectancy': '83.4'},
{'rank': '12', 'Country':'Costa Rica', 'Score': '7.167', 'GDP': '1.034', 'social_support':'1.441', 'freedom':'0.558', 'life_expectancy': '80.3'},
{'rank': '13', 'Country':'Israel', 'Score': '7.139', 'GDP': '1.276', 'social_support':'1.455', 'freedom':'0.371', 'life_expectancy': '83'},
{'rank': '14', 'Country':'Luxembourg', 'Score': '7.09', 'GDP': '1.609', 'social_support':'1.479', 'freedom':'0.526', 'life_expectancy': '82.3'},
{'rank': '15', 'Country':'United Kingdom', 'Score': '7.054', 'GDP': '1.333', 'social_support':'1.538', 'freedom':'0.45', 'life_expectancy': '81.3'},
{'rank': '16', 'Country':'Ireland', 'Score': '7.021', 'GDP': '1.499', 'social_support':'1.553', 'freedom':'0.516', 'life_expectancy': '82.3'},
{'rank': '17', 'Country':'Germany', 'Score': '6.985', 'GDP': '1.373', 'social_support':'1.454', 'freedom':'0.495', 'life_expectancy': '81.3'},
{'rank': '18', 'Country':'Belgium', 'Score': '6.923', 'GDP': '1.356', 'social_support':'1.504', 'freedom':'0.473', 'life_expectancy': '81.6'},
{'rank': '19', 'Country':'United States', 'Score': '6.892', 'GDP': '1.433', 'social_support':'1.457', 'freedom':'0.454', 'life_expectancy': '78.9'},
{'rank': '20', 'Country':'Czech Republic', 'Score': '6.852', 'GDP': '1.269', 'social_support':'1.487', 'freedom':'0.457', 'life_expectancy': '79.4'},
{'rank': '21', 'Country':'United Arab Emirates', 'Score': '6.825', 'GDP': '1.503', 'social_support':'1.31', 'freedom':'0.598', 'life_expectancy': '78'},
{'rank': '22', 'Country':'Malta', 'Score': '6.726', 'GDP': '1.3', 'social_support':'1.52', 'freedom':'0.564', 'life_expectancy': '59.3'},
{'rank': '23', 'Country':'Mexico', 'Score': '6.595', 'GDP': '1.07', 'social_support':'1.323', 'freedom':'0.433', 'life_expectancy': '75'},
{'rank': '24', 'Country':'France', 'Score': '6.592', 'GDP': '1.324', 'social_support':'1.472', 'freedom':'0.436', 'life_expectancy': '82.7'},
{'rank': '25', 'Country':'Taiwan', 'Score': '6.446', 'GDP': '1.368', 'social_support':'1.43', 'freedom':'0.351', 'life_expectancy': 'Not Available'},
{'rank': '26', 'Country':'Chile', 'Score': '6.444', 'GDP': '1.159', 'social_support':'1.369', 'freedom':'0.357', 'life_expectancy': '54.2'},
{'rank': '27', 'Country':'Guatemala', 'Score': '6.436', 'GDP': '0.8', 'social_support':'1.269', 'freedom':'0.535', 'life_expectancy': '74.3'},
{'rank': '28', 'Country':'Saudi Arabia', 'Score': '6.375', 'GDP': '1.403', 'social_support':'1.357', 'freedom':'0.439', 'life_expectancy': '75.1'},
{'rank': '29', 'Country':'Qatar', 'Score': '6.374', 'GDP': '1.684', 'social_support':'1.313', 'freedom':'0.555', 'life_expectancy': '80.2'},
{'rank': '30', 'Country':'Spain', 'Score': '6.354', 'GDP': '1.286', 'social_support':'1.484', 'freedom':'0.362', 'life_expectancy': '83.6'},
{'rank': '31', 'Country':'Panama', 'Score': '6.321', 'GDP': '1.149', 'social_support':'1.442', 'freedom':'0.516', 'life_expectancy': '78.5'},
{'rank': '32', 'Country':'Brazil', 'Score': '6.3', 'GDP': '1.004', 'social_support':'1.439', 'freedom':'0.39', 'life_expectancy': '75.9'},
{'rank': '33', 'Country':'Uruguay', 'Score': '6.293', 'GDP': '1.124', 'social_support':'1.465', 'freedom':'0.523', 'life_expectancy': '77.9'},
{'rank': '34', 'Country':'Singapore', 'Score': '6.262', 'GDP': '1.572', 'social_support':'1.463', 'freedom':'0.556', 'life_expectancy': '83.6'},
{'rank': '35', 'Country':'El Salvador', 'Score': '6.253', 'GDP': '0.794', 'social_support':'1.242', 'freedom':'0.43', 'life_expectancy': '73.3'},
{'rank': '36', 'Country':'Italy', 'Score': '6.223', 'GDP': '1.294', 'social_support':'1.488', 'freedom':'0.231', 'life_expectancy': '83.5'},
{'rank': '37', 'Country':'Bahrain', 'Score': '6.199', 'GDP': '1.362', 'social_support':'1.368', 'freedom':'0.536', 'life_expectancy': '77.3'},
{'rank': '38', 'Country':'Slovakia', 'Score': '6.198', 'GDP': '1.246', 'social_support':'1.504', 'freedom':'0.334', 'life_expectancy': '77.5'},
{'rank': '39', 'Country':'Trinidad & Tobago', 'Score': '6.192', 'GDP': '1.231', 'social_support':'1.477', 'freedom':'0.489', 'life_expectancy': '73.5'},
{'rank': '40', 'Country':'Poland', 'Score': '6.182', 'GDP': '1.206', 'social_support':'1.438', 'freedom':'0.483', 'life_expectancy': '78.7'},
{'rank': '41', 'Country':'Uzbekistan', 'Score': '6.174', 'GDP': '0.745', 'social_support':'1.529', 'freedom':'0.631', 'life_expectancy': '71.7'},
{'rank': '42', 'Country':'Lithuania', 'Score': '6.149', 'GDP': '1.238', 'social_support':'1.515', 'freedom':'0.291', 'life_expectancy': '75.9'},
{'rank': '43', 'Country':'Colombia', 'Score': '6.125', 'GDP': '0.985', 'social_support':'1.41', 'freedom':'0.47', 'life_expectancy': '77.3'},
{'rank': '44', 'Country':'Slovenia', 'Score': '6.118', 'GDP': '1.258', 'social_support':'1.523', 'freedom':'0.564', 'life_expectancy': '81.3'},
{'rank': '45', 'Country':'Nicaragua', 'Score': '6.105', 'GDP': '0.694', 'social_support':'1.325', 'freedom':'0.435', 'life_expectancy': '74.5'},
{'rank': '46', 'Country':'Kosovo', 'Score': '6.1', 'GDP': '0.882', 'social_support':'1.232', 'freedom':'0.489', 'life_expectancy': '72.25'},
{'rank': '47', 'Country':'Argentina', 'Score': '6.086', 'GDP': '1.092', 'social_support':'1.432', 'freedom':'0.471', 'life_expectancy': '76.7'},
{'rank': '48', 'Country':'Romania', 'Score': '6.07', 'GDP': '1.162', 'social_support':'1.232', 'freedom':'0.462', 'life_expectancy': '76'},
{'rank': '49', 'Country':'Cyprus', 'Score': '6.046', 'GDP': '1.263', 'social_support':'1.223', 'freedom':'0.406', 'life_expectancy': '81'},
{'rank': '50', 'Country':'Ecuador', 'Score': '6.028', 'GDP': '0.912', 'social_support':'1.312', 'freedom':'0.498', 'life_expectancy': '77'},
{'rank': '51', 'Country':'Kuwait', 'Score': '6.021', 'GDP': '1.5', 'social_support':'1.319', 'freedom':'0.493', 'life_expectancy': '75.5'},
{'rank': '52', 'Country':'Thailand', 'Score': '6.008', 'GDP': '1.05', 'social_support':'1.409', 'freedom':'0.557', 'life_expectancy': '77.2'},
{'rank': '53', 'Country':'Latvia', 'Score': '5.94', 'GDP': '1.187', 'social_support':'1.465', 'freedom':'0.264', 'life_expectancy': '75.3'},
{'rank': '54', 'Country':'South Korea', 'Score': '5.895', 'GDP': '1.301', 'social_support':'1.219', 'freedom':'0.159', 'life_expectancy': '83'},
{'rank': '55', 'Country':'Estonia', 'Score': '5.893', 'GDP': '1.237', 'social_support':'1.528', 'freedom':'0.495', 'life_expectancy': '78.8'},
{'rank': '56', 'Country':'Jamaica', 'Score': '5.89', 'GDP': '0.831', 'social_support':'1.478', 'freedom':'0.49', 'life_expectancy': '74.5'},
{'rank': '57', 'Country':'Mauritius', 'Score': '5.888', 'GDP': '1.12', 'social_support':'1.402', 'freedom':'0.498', 'life_expectancy': '75'},
{'rank': '58', 'Country':'Japan', 'Score': '5.886', 'GDP': '1.327', 'social_support':'1.419', 'freedom':'0.445', 'life_expectancy': '84.6'},
{'rank': '59', 'Country':'Honduras', 'Score': '5.86', 'GDP': '0.642', 'social_support':'1.236', 'freedom':'0.507', 'life_expectancy': '75.3'},
{'rank': '60', 'Country':'Kazakhstan', 'Score': '5.809', 'GDP': '1.173', 'social_support':'1.508', 'freedom':'0.41', 'life_expectancy': '73.6'},
{'rank': '61', 'Country':'Bolivia', 'Score': '5.779', 'GDP': '0.776', 'social_support':'1.209', 'freedom':'0.511', 'life_expectancy': '71.5'},
{'rank': '62', 'Country':'Hungary', 'Score': '5.758', 'GDP': '1.201', 'social_support':'1.41', 'freedom':'0.199', 'life_expectancy': '76.9'},
{'rank': '63', 'Country':'Paraguay', 'Score': '5.743', 'GDP': '0.855', 'social_support':'1.475', 'freedom':'0.514', 'life_expectancy': '74.3'},
{'rank': '64', 'Country':'Northern Cyprus', 'Score': '5.718', 'GDP': '1.263', 'social_support':'1.252', 'freedom':'0.417', 'life_expectancy': '75.8'},
{'rank': '65', 'Country':'Peru', 'Score': '5.697', 'GDP': '0.96', 'social_support':'1.274', 'freedom':'0.455', 'life_expectancy': '76.7'},
{'rank': '66', 'Country':'Portugal', 'Score': '5.693', 'GDP': '1.221', 'social_support':'1.431', 'freedom':'0.508', 'life_expectancy': '82'},
{'rank': '67', 'Country':'Pakistan', 'Score': '5.653', 'GDP': '0.677', 'social_support':'0.886', 'freedom':'0.313', 'life_expectancy': '67.3'},
{'rank': '68', 'Country':'Russia', 'Score': '5.648', 'GDP': '1.183', 'social_support':'1.452', 'freedom':'0.334', 'life_expectancy': '76'},
{'rank': '69', 'Country':'Philippines', 'Score': '5.631', 'GDP': '0.807', 'social_support':'1.293', 'freedom':'0.558', 'life_expectancy': '71.2'},
{'rank': '70', 'Country':'Serbia', 'Score': '5.603', 'GDP': '1.004', 'social_support':'1.383', 'freedom':'0.282', 'life_expectancy': '76'},
{'rank': '71', 'Country':'Moldova', 'Score': '5.529', 'GDP': '0.685', 'social_support':'1.328', 'freedom':'0.245', 'life_expectancy': '71.9'},
{'rank': '72', 'Country':'Libya', 'Score': '5.525', 'GDP': '1.044', 'social_support':'1.303', 'freedom':'0.416', 'life_expectancy': '72.9'},
{'rank': '73', 'Country':'Montenegro', 'Score': '5.523', 'GDP': '1.051', 'social_support':'1.361', 'freedom':'0.197', 'life_expectancy': '76.9'},
{'rank': '74', 'Country':'Tajikistan', 'Score': '5.467', 'GDP': '0.493', 'social_support':'1.098', 'freedom':'0.389', 'life_expectancy': '71.1'},
{'rank': '75', 'Country':'Croatia', 'Score': '5.432', 'GDP': '1.155', 'social_support':'1.266', 'freedom':'0.296', 'life_expectancy': '78.5'},
{'rank': '76', 'Country':'Hong Kong', 'Score': '5.43', 'GDP': '1.438', 'social_support':'1.277', 'freedom':'0.44', 'life_expectancy': '75.3'},
{'rank': '77', 'Country':'Dominican Republic', 'Score': '5.425', 'GDP': '1.015', 'social_support':'1.401', 'freedom':'0.497', 'life_expectancy': '74.1'},
{'rank': '78', 'Country':'Bosnia and Herzegovina', 'Score': '5.386', 'GDP': '0.945', 'social_support':'1.212', 'freedom':'0.212', 'life_expectancy': '77.4'},
{'rank': '79', 'Country':'Turkey', 'Score': '5.373', 'GDP': '1.183', 'social_support':'1.36', 'freedom':'0.195', 'life_expectancy': '77.7'},
{'rank': '80', 'Country':'Malaysia', 'Score': '5.339', 'GDP': '1.221', 'social_support':'1.171', 'freedom':'0.508', 'life_expectancy': '76.2'},
{'rank': '81', 'Country':'Belarus', 'Score': '5.323', 'GDP': '1.067', 'social_support':'1.465', 'freedom':'0.235', 'life_expectancy': '74.8'},
{'rank': '82', 'Country':'Greece', 'Score': '5.287', 'GDP': '1.181', 'social_support':'1.156', 'freedom':'0.067', 'life_expectancy': '82.2'},
{'rank': '83', 'Country':'Mongolia', 'Score': '5.285', 'GDP': '0.948', 'social_support':'1.531', 'freedom':'0.317', 'life_expectancy': '69.9'},
{'rank': '84', 'Country':'North Macedonia', 'Score': '5.274', 'GDP': '0.983', 'social_support':'1.294', 'freedom':'0.345', 'life_expectancy': '75.8'},
{'rank': '85', 'Country':'Nigeria', 'Score': '5.265', 'GDP': '0.696', 'social_support':'1.111', 'freedom':'0.426', 'life_expectancy': '54.7'},
{'rank': '86', 'Country':'Kyrgyzstan', 'Score': '5.261', 'GDP': '0.551', 'social_support':'1.438', 'freedom':'0.508', 'life_expectancy': '71.5'},
{'rank': '87', 'Country':'Turkmenistan', 'Score': '5.247', 'GDP': '1.052', 'social_support':'1.538', 'freedom':'0.394', 'life_expectancy': '68.2'},
{'rank': '88', 'Country':'Algeria', 'Score': '5.211', 'GDP': '1.002', 'social_support':'1.16', 'freedom':'0.086', 'life_expectancy': '76.9'},
{'rank': '89', 'Country':'Morocco', 'Score': '5.208', 'GDP': '0.801', 'social_support':'0.782', 'freedom':'0.418', 'life_expectancy': '76.7'},
{'rank': '90', 'Country':'Azerbaijan', 'Score': '5.208', 'GDP': '1.043', 'social_support':'1.147', 'freedom':'0.351', 'life_expectancy': '73'},
{'rank': '91', 'Country':'Lebanon', 'Score': '5.197', 'GDP': '0.987', 'social_support':'1.224', 'freedom':'0.216', 'life_expectancy': '78.9'},
{'rank': '92', 'Country':'Indonesia', 'Score': '5.192', 'GDP': '0.931', 'social_support':'1.203', 'freedom':'0.491', 'life_expectancy': '71.7'},
{'rank': '93', 'Country':'China', 'Score': '5.191', 'GDP': '1.029', 'social_support':'1.125', 'freedom':'0.521', 'life_expectancy': '76.9'},
{'rank': '94', 'Country':'Vietnam', 'Score': '5.175', 'GDP': '0.741', 'social_support':'1.346', 'freedom':'0.543', 'life_expectancy': '75.4'},
{'rank': '95', 'Country':'Bhutan', 'Score': '5.082', 'GDP': '0.813', 'social_support':'1.321', 'freedom':'0.457', 'life_expectancy': '71.8'},
{'rank': '96', 'Country':'Cameroon', 'Score': '5.044', 'GDP': '0.549', 'social_support':'0.91', 'freedom':'0.381', 'life_expectancy': '59.3'},
{'rank': '97', 'Country':'Bulgaria', 'Score': '5.011', 'GDP': '1.092', 'social_support':'1.513', 'freedom':'0.311', 'life_expectancy': '75'},
{'rank': '98', 'Country':'Ghana', 'Score': '4.996', 'GDP': '0.611', 'social_support':'0.868', 'freedom':'0.381', 'life_expectancy': '64.1'},
{'rank': '99', 'Country':'Ivory Coast', 'Score': '4.944', 'GDP': '0.569', 'social_support':'0.808', 'freedom':'0.352', 'life_expectancy': '83.5'},
{'rank': '100', 'Country':'Nepal', 'Score': '4.913', 'GDP': '0.446', 'social_support':'1.226', 'freedom':'0.439', 'life_expectancy': '70.8'},
{'rank': '101', 'Country':'Jordan', 'Score': '4.906', 'GDP': '0.837', 'social_support':'1.225', 'freedom':'0.383', 'life_expectancy': '74.5'},
{'rank': '102', 'Country':'Benin', 'Score': '4.883', 'GDP': '0.393', 'social_support':'0.437', 'freedom':'0.349', 'life_expectancy': '61.8'},
{'rank': '103', 'Country':'Congo (Brazzaville)', 'Score': '4.812', 'GDP': '0.673', 'social_support':'0.799', 'freedom':'0.372', 'life_expectancy': '64.3'},
{'rank': '104', 'Country':'Gabon', 'Score': '4.799', 'GDP': '1.057', 'social_support':'1.183', 'freedom':'0.295', 'life_expectancy': '66.5'},
{'rank': '105', 'Country':'Laos', 'Score': '4.796', 'GDP': '0.764', 'social_support':'1.03', 'freedom':'0.547', 'life_expectancy': '67.9'},
{'rank': '106', 'Country':'South Africa', 'Score': '4.722', 'GDP': '0.96', 'social_support':'1.351', 'freedom':'0.389', 'life_expectancy': '64.1'},
{'rank': '107', 'Country':'Albania', 'Score': '4.719', 'GDP': '0.947', 'social_support':'0.848', 'freedom':'0.383', 'life_expectancy': '78.6'},
{'rank': '108', 'Country':'Venezuela', 'Score': '4.707', 'GDP': '0.96', 'social_support':'1.427', 'freedom':'0.154', 'life_expectancy': '72.1'},
{'rank': '109', 'Country':'Cambodia', 'Score': '4.7', 'GDP': '0.574', 'social_support':'1.122', 'freedom':'0.609', 'life_expectancy': '69.8'},
{'rank': '110', 'Country':'Palestinian Territories', 'Score': '4.696', 'GDP': '0.657', 'social_support':'1.247', 'freedom':'0.225', 'life_expectancy': '74'},
{'rank': '111', 'Country':'Senegal', 'Score': '4.681', 'GDP': '0.45', 'social_support':'1.134', 'freedom':'0.292', 'life_expectancy': '67.9'},
{'rank': '112', 'Country':'Somalia', 'Score': '4.668', 'GDP': '0', 'social_support':'0.698', 'freedom':'0.559', 'life_expectancy': '54.4'},
{'rank': '113', 'Country':'Namibia', 'Score': '4.639', 'GDP': '0.879', 'social_support':'1.313', 'freedom':'0.401', 'life_expectancy': '63.7'},
{'rank': '114', 'Country':'Niger', 'Score': '4.628', 'GDP': '0.138', 'social_support':'0.774', 'freedom':'0.318', 'life_expectancy': '62.4'},
{'rank': '115', 'Country':'Burkina Faso', 'Score': '4.587', 'GDP': '0.331', 'social_support':'1.056', 'freedom':'0.255', 'life_expectancy': '61.6'},
{'rank': '116', 'Country':'Armenia', 'Score': '4.559', 'GDP': '0.85', 'social_support':'1.055', 'freedom':'0.283', 'life_expectancy': '75.1'},
{'rank': '117', 'Country':'Iran', 'Score': '4.548', 'GDP': '1.1', 'social_support':'0.842', 'freedom':'0.305', 'life_expectancy': '76.7'},
{'rank': '118', 'Country':'Guinea', 'Score': '4.534', 'GDP': '0.38', 'social_support':'0.829', 'freedom':'0.332', 'life_expectancy': '61.6'},
{'rank': '119', 'Country':'Georgia', 'Score': '4.519', 'GDP': '0.886', 'social_support':'0.666', 'freedom':'0.346', 'life_expectancy': '73.8'},
{'rank': '120', 'Country':'Gambia', 'Score': '4.516', 'GDP': '0.308', 'social_support':'0.939', 'freedom':'0.382', 'life_expectancy': '62'},
{'rank': '121', 'Country':'Kenya', 'Score': '4.509', 'GDP': '0.512', 'social_support':'0.983', 'freedom':'0.431', 'life_expectancy': '66.7'},
{'rank': '122', 'Country':'Mauritania', 'Score': '4.49', 'GDP': '0.57', 'social_support':'1.167', 'freedom':'0.066', 'life_expectancy': '64.9'},
{'rank': '123', 'Country':'Mozambique', 'Score': '4.466', 'GDP': '0.204', 'social_support':'0.986', 'freedom':'0.494', 'life_expectancy': '60.9'},
{'rank': '124', 'Country':'Tunisia', 'Score': '4.461', 'GDP': '0.921', 'social_support':'1', 'freedom':'0.167', 'life_expectancy': '76.7'},
{'rank': '125', 'Country':'Bangladesh', 'Score': '4.456', 'GDP': '0.562', 'social_support':'0.928', 'freedom':'0.527', 'life_expectancy': '72.6'},
{'rank': '126', 'Country':'Iraq', 'Score': '4.437', 'GDP': '1.043', 'social_support':'0.98', 'freedom':'0.241', 'life_expectancy': '70.6'},
{'rank': '127', 'Country':'Congo (Kinshasa)', 'Score': '4.418', 'GDP': '0.094', 'social_support':'1.125', 'freedom':'0.269', 'life_expectancy': '64.3'},
{'rank': '128', 'Country':'Mali', 'Score': '4.39', 'GDP': '0.385', 'social_support':'1.105', 'freedom':'0.327', 'life_expectancy': '59.3'},
{'rank': '129', 'Country':'Sierra Leone', 'Score': '4.374', 'GDP': '0.268', 'social_support':'0.841', 'freedom':'0.309', 'life_expectancy': '54.7'},
{'rank': '130', 'Country':'Sri Lanka', 'Score': '4.366', 'GDP': '0.949', 'social_support':'1.265', 'freedom':'0.47', 'life_expectancy': '77'},
{'rank': '131', 'Country':'Myanmar', 'Score': '4.36', 'GDP': '0.71', 'social_support':'1.181', 'freedom':'0.525', 'life_expectancy': '67.1'},
{'rank': '132', 'Country':'Chad', 'Score': '4.35', 'GDP': '0.35', 'social_support':'0.766', 'freedom':'0.174', 'life_expectancy': '54.2'},
{'rank': '133', 'Country':'Ukraine', 'Score': '4.332', 'GDP': '0.82', 'social_support':'1.39', 'freedom':'0.178', 'life_expectancy': '72.1'},
{'rank': '134', 'Country':'Ethiopia', 'Score': '4.286', 'GDP': '0.336', 'social_support':'1.033', 'freedom':'0.344', 'life_expectancy': '66.6'},
{'rank': '135', 'Country':'Swaziland', 'Score': '4.212', 'GDP': '0.811', 'social_support':'1.149', 'freedom':'0.313', 'life_expectancy': '71.7'},
{'rank': '136', 'Country':'Uganda', 'Score': '4.189', 'GDP': '0.332', 'social_support':'1.069', 'freedom':'0.356', 'life_expectancy': '63.4'},
{'rank': '137', 'Country':'Egypt', 'Score': '4.166', 'GDP': '0.913', 'social_support':'1.039', 'freedom':'0.241', 'life_expectancy': '72'},
{'rank': '138', 'Country':'Zambia', 'Score': '4.107', 'GDP': '0.578', 'social_support':'1.058', 'freedom':'0.431', 'life_expectancy': '63.9'},
{'rank': '139', 'Country':'Togo', 'Score': '4.085', 'GDP': '0.275', 'social_support':'0.572', 'freedom':'0.293', 'life_expectancy': '61'},
{'rank': '140', 'Country':'India', 'Score': '4.015', 'GDP': '0.755', 'social_support':'0.765', 'freedom':'0.498', 'life_expectancy': '69.7'},
{'rank': '141', 'Country':'Liberia', 'Score': '3.975', 'GDP': '0.073', 'social_support':'0.922', 'freedom':'0.37', 'life_expectancy': '64.1'},
{'rank': '142', 'Country':'Comoros', 'Score': '3.973', 'GDP': '0.274', 'social_support':'0.757', 'freedom':'0.142', 'life_expectancy': '64.3'},
{'rank': '143', 'Country':'Madagascar', 'Score': '3.933', 'GDP': '0.274', 'social_support':'0.916', 'freedom':'0.148', 'life_expectancy': '67'},
{'rank': '144', 'Country':'Lesotho', 'Score': '3.802', 'GDP': '0.489', 'social_support':'1.169', 'freedom':'0.359', 'life_expectancy': '54.3'},
{'rank': '145', 'Country':'Burundi', 'Score': '3.775', 'GDP': '0.046', 'social_support':'0.447', 'freedom':'0.22', 'life_expectancy': '61.6'},
{'rank': '146', 'Country':'Zimbabwe', 'Score': '3.663', 'GDP': '0.366', 'social_support':'1.114', 'freedom':'0.361', 'life_expectancy': '61.5'},
{'rank': '147', 'Country':'Haiti', 'Score': '3.597', 'GDP': '0.323', 'social_support':'0.688', 'freedom':'0.026', 'life_expectancy': '64'},
{'rank': '148', 'Country':'Botswana', 'Score': '3.488', 'GDP': '1.041', 'social_support':'1.145', 'freedom':'0.455', 'life_expectancy': '69.6'},
{'rank': '149', 'Country':'Syria', 'Score': '3.462', 'GDP': '0.619', 'social_support':'0.378', 'freedom':'0.013', 'life_expectancy': 'Not Available'},
{'rank': '150', 'Country':'Malawi', 'Score': '3.41', 'GDP': '0.191', 'social_support':'0.56', 'freedom':'0.443', 'life_expectancy': '64.3'},
{'rank': '151', 'Country':'Yemen', 'Score': '3.38', 'GDP': '0.287', 'social_support':'1.163', 'freedom':'0.143', 'life_expectancy': '66.1'},
{'rank': '152', 'Country':'Rwanda', 'Score': '3.334', 'GDP': '0.359', 'social_support':'0.711', 'freedom':'0.555', 'life_expectancy': '69'},
{'rank': '153', 'Country':'Tanzania', 'Score': '3.231', 'GDP': '0.476', 'social_support':'0.885', 'freedom':'0.417', 'life_expectancy': '65.5'},
{'rank': '154', 'Country':'Afghanistan', 'Score': '3.203', 'GDP': '0.35', 'social_support':'0.517', 'freedom':'0', 'life_expectancy': '64.8'},
{'rank': '155', 'Country':'Central African Republic', 'Score': '3.083', 'GDP': '0.026', 'social_support':'0', 'freedom':'0.225', 'life_expectancy': '73'},
{'rank': '156', 'Country':'South Sudan', 'Score': '2.853', 'GDP': '0.306', 'social_support':'0.575', 'freedom':'0.01', 'life_expectancy': '57.9'}

    ]
)


# Set route
@app.route('/')
def index():
    # Store the entire team collection in a list
    happinesss = list(db.happiness.find())
    print(happinesss)

    # Return the template with the teams list passed in
    return render_template('Data.html', happinesss=happinesss)


if __name__ == "__main__":
    app.run(debug=True)
