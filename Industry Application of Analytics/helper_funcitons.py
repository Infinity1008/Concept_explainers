# ---------------------------------------------------------------------------------------- # 
import numpy as np
import matplotlib.pyplot as plt


def draw_line(slope, intercept):    
    
    # Setting up a cartesian plane
    plt.figure(figsize=(8,8))
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    # ----------------------------------------------------------

    """Plot a line from slope and intercept"""
    x = np.linspace(-100,100,100)    
    abline_values = slope * x + intercept
    # ----------------------------------------------------------
    

    
    # Plotting the lines
    #     f, ax = plt.subplots()
    plt.xlim([-5,5])
    plt.ylim([-5,5])
    plt.plot(x, abline_values, '-')
    plt.grid()
    # ----------------------------------------------------------

    # Plotting lines for x = 1
    value_of_y_for_1 = slope * 1 + intercept    
    
    plt.plot([1, 1], [0, value_of_y_for_1], linestyle='--')
    plt.plot([0, 1], [value_of_y_for_1, value_of_y_for_1], linestyle='--')
    # ----------------------------------------------------------


    # Plotting lines for x = -3
    value_of_y_for_3 = slope * -3 + intercept    
    
    plt.plot([-3, -3], [0, value_of_y_for_3], linestyle='--')
    plt.plot([0, -3], [value_of_y_for_3, value_of_y_for_3], linestyle='--')
    # ----------------------------------------------------------
    
    
    # Plotting texts for values of x and y 
    plt.text(1.2,value_of_y_for_1-value_of_y_for_1/2, f'y={round(value_of_y_for_1,2)}', fontsize = 12)
    plt.text(0.3,value_of_y_for_1+0.3, f'x={1}', fontsize = 12)
    # ----------------------------------------------------------

    # Plotting texts for values of x and y 
    plt.text(-4,value_of_y_for_3/2, f'y={round(value_of_y_for_3,2)}', fontsize = 12)
    plt.text(-3/2,value_of_y_for_3*1.2, f'x={-3}', fontsize = 12)
    # ----------------------------------------------------------
    
    # Plotting texts for legend
    plt.text(.01, .99, f'Slope = {slope}', ha='left', va='top', transform=ax.transAxes)
    plt.text(.01, .95, f'Intecept = {intercept}', ha='left', va='top', transform=ax.transAxes)
    # ----------------------------------------------------------

    plt.text(.01, .90, f'y = {slope}*x + {intercept}', ha='left', va='top', transform=ax.transAxes)
    plt.text(.01, .86, f'y = {value_of_y_for_1}', ha='left', va='top', transform=ax.transAxes)
    plt.show()
    # ----------------------------------------------------------

# ---------------------------------------------------------------------------------------- # 

def plot_our_data():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    size = [3,5,12,7,10,9,4,13,7,11]
    weights = [4,7,14,5,12,8,7,18,5,8]
    # ----------------------------------------------------------

    # Plotting data
    plt.scatter(weights, size) 
    plt.grid()
    # ----------------------------------------------------------

    plt.xlim([0,20])
    plt.ylim([0,20])
    # ----------------------------------------------------------

    plt.title('Generating Our Weight & Size data')
    plt.xlabel('Weight')
    plt.ylabel('Size')
    plt.show()
    # ----------------------------------------------------------
    

def plot_data_and_line(slope,intercept):

    size = [3,5,12,7,10,9,4,13,7,11]
    weights = [4,7,14,5,12,8,7,18,5,8]
    # ----------------------------------------------------------
    
    
    plt.figure(figsize=(7,7))
    ax = plt.gca()
    
    plt.scatter(weights, size) # Plotting data
    # ----------------------------------------------------------

    plt.title('Plotting our Data & Line')
    plt.xlabel('Weights')
    plt.ylabel('Size')
    # ----------------------------------------------------------
    
    x = np.array(range(1,20))
    x = x.reshape(-1,1)
    
    # ----------------------------------------------------------
    # Plotting a line
    abline_values = slope * x + intercept
    
    # Plot the best fit line over the actual values    
    plt.xlim([0,20])
    plt.ylim([0,20])
    plt.plot(x, abline_values, '-')
    plt.grid()
    # ----------------------------------------------------------
    
#     # Plotting lines for x = 1
    value_of_y_for_10 = slope * 10 + intercept    
    
    plt.plot([10, 10], [0, value_of_y_for_10], linestyle='--')
    plt.plot([0, 10], [value_of_y_for_10, value_of_y_for_10], linestyle='--')
    
    
    # Plotting texts for values of x and y 
    plt.text(10, value_of_y_for_10/2, f' For weight 10 with \n slope={slope} & intercept={intercept}', fontsize = 8)
    plt.text(10/4,value_of_y_for_10+0.5, f' Our prediction for \ny will be {value_of_y_for_10}', fontsize = 8)
    # ----------------------------------------------------------

    
    plt.text(.01, .99, f'Slope = {slope}', ha='left', va='top', transform=ax.transAxes)
    plt.text(.01, .95, f'Intecept = {intercept}', ha='left', va='top', transform=ax.transAxes)
    plt.text(.01, .90, f'y = {slope}*x + {intercept}', ha='left', va='top', transform=ax.transAxes)


    plt.show()
    # ----------------------------------------------------------

# ---------------------------------------------------------------------------------------- # 


def plot_data_line_residuals_ssr(slope,intercept):

    size = [3,5,12,7,10,9,4,13,7,11]
    weights = [4,7,14,5,12,8,7,20,5,8]
    # ----------------------------------------------------------

    plt.figure(figsize=(7,7))
    ax = plt.gca()

    plt.scatter(weights, size) # Plotting data
    # ----------------------------------------------------------

    plt.title('Plotting our Data & Line')
    plt.xlabel('Weights')
    plt.ylabel('Size')
    # ----------------------------------------------------------

    x = np.array(range(1,25))
    x = x.reshape(-1,1)

    # ----------------------------------------------------------
    # Plotting a line
    abline_values = slope * x + intercept

    # Plot the best fit line over the actual values    
    plt.xlim([0, 25])
    plt.ylim([0,25])
    plt.plot(x, abline_values, '-')
    plt.grid()
    # ----------------------------------------------------------

    def calculate_y(x):
        y = x*slope + intercept
        return y
    # ----------------------------------------------------------

    # Plotting residual lines 
    for i in range(len(size)):
        plt.plot((weights[i],weights[i]),(size[i],calculate_y(weights[i])), '--')
    # ----------------------------------------------------------

    # Plotting residuals text
    for i in range(0,len(size),2):
        a = weights[i]
        b = calculate_y(size[i])

        c = b + (a-b)/2
        plt.text(size[i],c, 'Residual', fontsize = 8)

    # ----------------------------------------------------------
        
    # Calculating SSR
    predicted_values = np.array([calculate_y(i) for i in weights]) 
    ssr = np.sum(np.square(np.array(size) - predicted_values))
    
    # ----------------------------------------------------------

    plt.text(.01, .99, f'Slope = {slope}', ha='left', va='top', transform=ax.transAxes)
    plt.text(.01, .95, f'Intecept = {intercept}', ha='left', va='top', transform=ax.transAxes)
    # ----------------------------------------------------------
    
    plt.text(.01, .90, f'y = {slope}*x + {intercept}', ha='left', va='top', transform=ax.transAxes)
    plt.text(1, .5, f'  Variance = {round(ssr)}', ha='left', va='top', fontsize= 'large',transform=ax.transAxes)
    # ----------------------------------------------------------

    plt.show()

# ---------------------------------------------------------------------------------------- # 


def create_data_line_residuals_rmse(slope,intercept):

    size = [3,5,12,7,10,9,4,13,7,11]
    weights = [4,7,14,5,12,8,7,20,5,8]
    # ----------------------------------------------------------

    plt.figure(figsize=(7,7))
    ax = plt.gca()

    plt.scatter(weights, size) # Plotting data
    # ----------------------------------------------------------

    plt.title('Plotting our Data & Line')
    plt.xlabel('Weights')
    plt.ylabel('Size')
    # ----------------------------------------------------------

    x = np.array(range(1,25))
    x = x.reshape(-1,1)

    # ----------------------------------------------------------
    # Plotting a line
    abline_values = slope * x + intercept

    # Plot the best fit line over the actual values    
    plt.xlim([0, 25])
    plt.ylim([0,25])
    plt.plot(x, abline_values, '-')
    plt.grid()
    # ----------------------------------------------------------

    def calculate_y(x):
        y = x*slope + intercept
        return y
    # ----------------------------------------------------------

    # Plotting residual lines 
    for i in range(len(size)):
        plt.plot((weights[i],weights[i]),(size[i],calculate_y(weights[i])), '--')
    # ----------------------------------------------------------

    # Plotting residuals text
    for i in range(0,len(size),2):
        a = weights[i]
        b = calculate_y(size[i])

        c = b + (a-b)/2
        plt.text(size[i],c, 'Residual', fontsize = 8)

    # ----------------------------------------------------------
        
    # Calculating SSR
    predicted_values = np.array([calculate_y(i) for i in weights]) 
#     ssr = np.sum(np.square(np.array(size) - predicted_values))
    
    rmse = np.sqrt(np.mean((predicted_values-np.array(size))**2))
    
    # ----------------------------------------------------------

    plt.text(.01, .99, f'Slope = {slope}', ha='left', va='top', transform=ax.transAxes)
    plt.text(.01, .95, f'Intecept = {intercept}', ha='left', va='top', transform=ax.transAxes)
    # ----------------------------------------------------------
    
    plt.text(.01, .90, f'y = {slope}*x + {intercept}', ha='left', va='top', transform=ax.transAxes)
    plt.text(1, .5, f'  RMSE = {round(rmse,3)}', ha='left', va='top', fontsize= 'large',transform=ax.transAxes)
    # ----------------------------------------------------------

    plt.show()

# ---------------------------------------------------------------------------------------- # 




