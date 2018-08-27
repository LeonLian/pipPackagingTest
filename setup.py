import setuptools

setuptools.setup(
    name='myFirstPIP',
    version='0.1',
    author="lian zheng",
    author_email="lianzheng07@163.com",
    description="This is my first pip package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LeonLian/pipPackagingTest.git",
    scripts=['helloworld.py']
)









