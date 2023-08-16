# karaoke_lyric
Final Udacity Project

1. Idea of CICD pipeline
- karaoke_lyric project will be pushed to github
- CircleCi will fetch the latest commit:
    + build IaaC on AWS: EC2
    + build docker on CircleCI
    + copy docker to EC2 using ansible
    + run kubernete on EC2
2. Test pipeline
- UnitTest phase
- SmokeTest phase