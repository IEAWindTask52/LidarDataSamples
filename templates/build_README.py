# template readme
with open('templates/README.stub') as f:
    readme_stub = f.read()

with open('LidarDataSamples.md') as t:
    data_table = t.read()

# simple replacement, use whatever stand-in value is useful for you.
readme = readme_stub.replace('{LidarDataSamples}', data_table)

with open('README.md', 'w') as f:
    f.write(readme)
