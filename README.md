# karaoke_lyric Project
https://github.com/lqdung95ntp/karaoke_lyric

Final Udacity Project

1. Idea of CICD pipeline
- Karaoke_lyric project will be pushed to github
- CircleCi will fetch the latest commit:
    + Build IaaS on AWS using Cloudformation
![alt cloudformation](./screenshot/3.Cloudformation_IaaS.png)
    + Instance EC2 is created:
![alt ec2_created](./screenshot/3.EC2_IaaS.png)
    + Build CircleCI pipeline
![alt circleci](./screenshot/4.CircleCI_Pipeline.png)
    + Push the docker image to the repository
![alt pushdocker](./screenshot/4.Push_Docker.png)
    + Deploy app using Kubernetes:
![alt deploy_kubectl](./screenshot/5.Deploy_Kubernetes.png)
    + Access webapp using public link: http://54.146.58.147:8080/login?next=/personal
![alt public_webapp](./screenshot/6.Public_Website.png)
2. Test pipeline
- Lint fail test
![alt hadolint_fail](./screenshot/1.Hadolint_Fail.png)
- Lint pass test
![alt hadolint_pass](./screenshot/2.Hadolint_Pass.png)