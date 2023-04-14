import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

sentiment_scores = [{'label': 'neutral', 'score': 0.7108820080757141},                    {'label': 'negative', 'score': 0.5155061483383179},                    {'label': 'neutral', 'score': 0.4959917962551117},                    {'label': 'neutral', 'score': 0.7584750652313232},                    {'label': 'positive', 'score': 0.6433528661727905},                    {'label': 'neutral', 'score': 0.7857950925827026},                    {'label': 'neutral', 'score': 0.4486306607723236},                    {'label': 'neutral', 'score': 0.743915319442749},                    {'label': 'neutral', 'score': 0.8410157561302185},                    {'label': 'neutral', 'score': 0.8730957508087158},                    {'label': 'neutral', 'score': 0.7833043932914734},                    {'label': 'neutral', 'score': 0.8343775868415833},                    {'label': 'neutral', 'score': 0.7712959051132202},                    {'label': 'neutral', 'score': 0.776803731918335},                    {'label': 'neutral', 'score': 0.8200016021728516},                    {'label': 'neutral', 'score': 0.6157656908035278},                    {'label': 'neutral', 'score': 0.8190017938613892},                    {'label': 'neutral', 'score': 0.7150989770889282},                    {'label': 'neutral', 'score': 0.7759681940078735},                    {'label': 'neutral', 'score': 0.7375119924545288},                    {'label': 'neutral', 'score': 0.48532310128211975},                    {'label': 'positive', 'score': 0.4630918502807617},                    {'label': 'positive', 'score': 0.6873413324356079},                    {'label': 'neutral', 'score': 0.6023297309875488},                    {'label': 'neutral', 'score': 0.4999650716781616},                    {'label': 'negative', 'score': 0.5476510524749756},                    {'label': 'positive', 'score': 0.5904302597045898}]

# Initialize empty lists for x (indices), y (score values), and colors
x = []
y = []
colors = []

# Loop through the sentiment scores and append the index, score value, and color to the respective lists
for i, score in enumerate(sentiment_scores):
    x.append(i)
    y.append(score['score'])
    if score['label'] == 'positive':
        colors.append('green')
    elif score['label'] == 'negative':
        colors.append('red')
    else:
        colors.append('grey')

# Create the bar plot
plt.bar(x, y, color=colors)

# Add axis labels and title
plt.xlabel('Sentiment Analysis Result for 2022frank_01')
plt.ylabel('Score Value')
plt.title('Sentiment Analysis Scores')

# Customize the plot
plt.xticks(x, [f" {i+1}" for i in x], rotation=45)
plt.ylim([0, 1])
plt.grid(axis='y', alpha=0.5)

# Show the plot
plt.show()
plt.savefig("2022_frank01.plot.png")





