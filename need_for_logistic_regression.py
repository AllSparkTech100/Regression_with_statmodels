# Create the histograms of time_since_last_purchase split by has_churned
sns.displot(data=churn, x='time_since_last_purchase', col='has_churned')

plt.show()



# Draw a linear regression trend line and a scatter plot of time_since_first_purchase vs. has_churned
sns.regplot(x='time_since_first_purchase',
           y='has_churned', data=churn, line_kws={"color": "red"})

plt.show()



# Redraw the plot with time_since_first_purchase
sns.displot(x='time_since_first_purchase', col='has_churned', data=churn)

plt.show()




# Draw a linear regression trend line and a scatter plot of time_since_first_purchase vs. has_churned
sns.regplot(x="time_since_first_purchase",
            y="has_churned",
            data=churn, 
            ci=None,
            line_kws={"color": "red"})

# Draw a logistic regression trend line and a scatter plot of time_since_first_purchase vs. has_churned
sns.regplot(x='time_since_first_purchase', y='has_churned', data=churn, logistic=True, ci=None, line_kws={'color': 'blue'})

plt.show()