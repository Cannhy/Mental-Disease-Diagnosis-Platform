from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
import datetime


# Create your views here.
class PublicRegister(APIView):
    def get(self, request):
        userNickname = str(request.GET.get("nickName", None))
        userName = str(request.GET.get("userName", None))
        userPassword = str(request.GET.get("userPassword", None))
        userPassword2 = str(request.GET.get("userPassword2", None))
        res = Public.objects.filter(id=userName)
        flag = res.exists()
        if flag:
            return Response(1)
        elif userPassword != userPassword2:
            return Response(2)
        else:
            public = Public(id=userName, name=userNickname, password=userPassword)
            public.save()
            return Response(0)


class PublicLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get("userName", None))
        userPassword = str(request.GET.get("userPassword", None))
        res = Public.objects.filter(id=userName)
        flag = res.exists()
        if flag:
            if res[0].password == userPassword:
                return Response(dict([("ret", 0), ("nickName", res[0].name)]))
            else:
                return Response(dict([("ret", 1)]))
        else:
            return Response(dict([("ret", 2)]))


class DoctorRegister(APIView):
    def get(self, request):
        userNickname = str(request.GET.get("nickName", None))
        userName = str(request.GET.get("userName", None))
        userPassword = str(request.GET.get("userPassword", None))
        userPassword2 = str(request.GET.get("userPassword2", None))
        res = Doctor.objects.filter(id=userName)
        flag = res.exists()
        if flag:
            return Response(1)
        elif userPassword != userPassword2:
            return Response(2)
        else:
            doctor = Doctor(id=userName, name=userNickname, password=userPassword)
            doctor.save()
            return Response(0)


class DoctorLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get("userName", None))
        userPassword = str(request.GET.get("userPassword", None))
        res = Doctor.objects.filter(id=userName)
        flag = res.exists()
        if flag:
            if res[0].password == userPassword:
                return Response(dict([("ret", 0), ("nickName", res[0].name)]))
            else:
                return Response(dict([("ret", 1)]))
        else:
            return Response(dict([("ret", 2)]))


class ScientistRegister(APIView):
    def get(self, request):
        userNickname = str(request.GET.get("nickName", None))
        userName = str(request.GET.get("userName", None))
        userPassword = str(request.GET.get("userPassword", None))
        userPassword2 = str(request.GET.get("userPassword2", None))
        res = Researcher.objects.filter(id=userName)
        flag = res.exists()
        if flag:
            return Response(1)
        elif userPassword != userPassword2:
            return Response(2)
        else:
            researcher = Researcher(
                id=userName, name=userNickname, password=userPassword
            )
            researcher.save()
            return Response(0)


class ScientistLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get("userName", None))
        userPassword = str(request.GET.get("userPassword", None))
        res = Researcher.objects.filter(id=userName)
        flag = res.exists()
        if flag:
            if res[0].password == userPassword:
                return Response(dict([("ret", 0), ("nickName", res[0].name)]))
            else:
                return Response(dict([("ret", 1)]))
        else:
            return Response(dict([("ret", 2)]))


class getPublicResume(APIView):
    def get(self, request):
        userName = str(request.GET.get("userName", None))
        # userPassword = str(request.GET.get('userPassword', None))
        ans = []
        res = Public.objects.filter(id=userName)
        for i in res:
            ans.append(
                {
                    "id": i.id,
                    "name": i.name,
                    "gender": i.gender,
                    "age": i.age,
                    "history": i.history,
                    "birthdate": i.birthdate,
                    "region": i.region,
                    "education": i.education,
                    "phone": i.phone,
                    "ApoE": i.ApoE,
                    "ID": i.identy,
                    "MMSE": i.MMSE,
                    "CDR_Global": i.CDR_Global,
                    "CDR_SOB": i.CDR_SOB,
                    "ADAS_Cog": i.ADAS_Cog,
                    "MRI": i.MRI,
                    "PET": i.PET,
                }
            )
        return Response(ans[0])


class publicSaveResume(APIView):
    def get(self, request):
        userName = str(request.GET.get("userName"))
        userNickname = str(request.GET.get("nickName", ''))
        userGender = str(request.GET.get("userGender", ''))
        userAge = str(request.GET.get("userAge", ''))
        userBirthdate = str(request.GET.get("userBirthdate", ''))
        userRegion = str(request.GET.get("userRegion", ''))
        userEducation = str(request.GET.get("userEducation", ''))
        userPhone = str(request.GET.get("userPhone", ''))
        userApoE = str(request.GET.get("userApoE", ''))
        userMMSE = str(request.GET.get("userMMSE", ''))
        userCDR_Global = str(request.GET.get("userCDR_Global", ''))
        userCDR_SOB = str(request.GET.get("userCDR_SOB", ''))
        userADAS_Cog = str(request.GET.get("userADAS_Cog", ''))
        userMRI = str(request.GET.get("userMRI", ''))
        userPET = str(request.GET.get("userPET", ''))
        identy = str(request.GET.get("userID", ''))
        public = Public.objects.filter(id=userName).first()
        print("asdadawdwadwad\n")
        print(request.data)
        print("asdadawdwadwad\n")
        public.name = userNickname
        public.gender = userGender
        public.age = userAge
        public.identy = identy
        public.birthdate = userBirthdate
        public.region = userRegion
        public.education = userEducation
        public.phone = userPhone
        public.ApoE = userApoE
        public.MMSE = userMMSE
        public.CDR_Global = userCDR_Global
        public.CDR_SOB = userCDR_SOB
        public.ADAS_Cog = userADAS_Cog
        public.MRI = userMRI
        public.PET = userPET
        public.save()
        return Response(0)


class getPublicDiagnosisList(APIView):
    def get(self, request):
        userName = str(request.GET.get("userName", None))
        res = DiagnosisMission.objects.filter(patient_id=userName)
        ans = []
        for i in res:
            if i.researcherEstablish == "否":
                ans.append(
                    {
                        "id": i.id,
                        "name": i.name,
                        "startTime": i.startTime,
                        "endTime": i.endTime,
                        "content": i.resultDisease + '-' + i.resultStage,
                        "finishState": i.state,
                        "notifyState": i.whetherPublic,
                    }
                )
        return Response(ans)


class publicEstablishDiagnosis(APIView):
    def get(self, request):
        userName = str(request.GET.get("userName", None))
        description = str(request.GET.get("describe", None))
        disorder = str(request.GET.get("disorder", None))
        taskName = str(request.GET.get("taskName", None))
        missionNum = DiagnosisMission.objects.all().count()
        res = Public.objects.get(id=userName)
        patientName = res.name
        diagnosisMission = DiagnosisMission(
            id=missionNum + 1,
            name=taskName,
            patient_id_id=userName,
            patient_name=patientName,
            researcherEstablish="否",
            whetherPublic="否",
            startTime=datetime.datetime.now(),
            endTime=datetime.datetime.now(),
            description=description,
            state="已完成",
            data="默认数据集",
            model="默认模型",
            scene=disorder,
        )
        diagnosisMission.save()
        return Response(0)


class publicLaunchPridict(APIView):
    def get(self, request):
        userName = str(request.GET.get("userName", None))
        disorder = str(request.GET.get("disorder", None))
        introduction = str(request.GET.get("introduction", None))
        taskName = str(request.GET.get("taskName", None))
        missonNum = PredictMission.objects.all().count()
        res = Public.objects.get(id=userName)
        patientName = res.name
        predictMission = PredictMission(
            id=missonNum + 1,
            name=taskName,
            patient_id_id=userName,
            patient_name=patientName,
            researcherEstablish="否",
            whetherPublic="否",
            startTime=datetime.datetime.now(),
            endTime=datetime.datetime.now(),
            state="已完成",
            description=introduction,
            data="默认数据集",
            model="默认模型",
            scene=disorder,
        )
        predictMission.save()
        return Response(0)


class getPublicPredictList(APIView):
    def get(self, request):
        userName = str(request.GET.get("userName", None))
        res = PredictMission.objects.filter(patient_id=userName)
        ans = []
        for i in res:
            if i.researcherEstablish == "否":
                ans.append(
                    {
                        "id": i.id,
                        "name": i.name,
                        "startTime": i.startTime,
                        "endTime": i.endTime,
                        "risk": i.risk,
                        "finishState": i.state,
                        "notifyState": i.whetherPublic,
                    }
                )
        return Response(ans)


class getPublicRecmmendation(APIView):
    def get(self, request):
        userName = str(request.GET.get("userName", None))
        res = PlanRecommendMission.objects.filter(patient_id=userName)
        ans = []
        for i in res:
            if i.researcherEstablish == "否":
                ans.append({"scheme": i.plan, "state": True if i.whetherPublic == '是' else False})
        if len(ans) == 0:
            ans.append({"scheme": '', "state": False})
        return Response(ans[0])


class getDatasetList(APIView):
    def get(self, request):
        res = Data.objects.all()
        ans = []
        for i in res:
            ans.append(
                {
                    "id": i.id,
                    "name": i.name,
                    "ownerID": i.ownerID,
                    "ownerName": i.ownerName,
                    "time": i.time,
                    "size": i.size,
                    "scenes": i.scene,
                    "introduction": i.description,
                    "model": i.model
                }
            )
        return Response(ans)


class uploadDataset(APIView):
    def get(self, request):
        name = str(request.GET.get("name", None))
        introduction = str(request.GET.get("introduction", None))
        scene = str(request.GET.get("scene", None))
        model = str(request.GET.get("model", None))
        ownerName = str(request.GET.get("ownerName", None))
        ownerID = str(request.GET.get("ownerID", None))
        datasetNum = Data.objects.all().count()
        # dataLoad = request.FILES.get('file')
        # size = dataLoad.size
        size = "56.3GB"
        data = Data(
            id=datasetNum + 1,
            name=name,
            scene=scene,
            description=introduction,
            model=model,
            time=datetime.datetime.now(),
            size=size,
            ownerName=ownerName,
            ownerID=ownerID
        )
        data.save()
        return Response(0)


class DeleteDataset(APIView):
    def get(self, request):
        id = str(request.GET.get("datasetID", None))
        data = Data.objects.get(id=id)
        data.delete()
        return Response(0)


class getModelList(APIView):
    def get(self, request):
        res = BigModel.objects.all()
        ans = []
        for i in res:
            ans.append(
                {
                    "id": i.id,
                    "name": i.name,
                    "type": i.type,
                    "ownerID": i.ownerID,
                    "ownerName": i.ownerName,
                    "time": datetime.datetime.now(),
                    "scenes": i.scene,
                    "data": i.data,
                    "introduction": i.description,
                }
            )
        return Response(ans)


class getPatientsList(APIView):
    def get(self, request):
        res = Public.objects.all()
        ans = []
        for i in res:
            ans.append(
                {
                    "id": i.id,
                    "name": i.name,
                    "gender": i.gender,
                    "age": i.age,
                    "birthdate": i.birthdate,
                    "region": i.region,
                    "education": i.education,
                    "phone": i.phone,
                    "ID": i.identy,
                    "ApoE": i.ApoE,
                    "history": i.history,
                    "MMSE": i.MMSE,
                    "CDR_Global": i.CDR_Global,
                    "CDR_SOB": i.CDR_SOB,
                    "ADAS_Cog": i.ADAS_Cog,
                    "MRI": i.MRI,
                    "PET": i.PET,
                }
            )
        return Response(ans)


class getPatientAssistantTask(APIView):
    def get(self, request):
        patientID = str(request.GET.get("patientID", None))
        res = DiagnosisMission.objects.filter(patient_id=patientID)
        ans = []
        for i in res:
            ans.append(
                {
                    "id": i.id,
                    "name": i.name,
                    "state": i.state,
                    "startTime": i.startTime,
                    "endTime": i.endTime,
                    "introduction": i.description,
                    "scene": i.scene,
                    "data": i.data,
                    "model": i.model,
                    "result": i.result,
                }
            )
        return Response(ans)


class getBoardsList(APIView):
    def get(self, request):
        res = RecordTemplate.objects.all()
        ans = []
        for i in res:
            ans.append(
                {
                    "id": i.id,
                    "name": i.name,
                    "doctorID": i.ownerID,
                    "doctorName": i.ownerName,
                    "time": i.time,
                    "introduction": i.description,
                    "scenes": i.scene,
                }
            )
        return Response(ans)


class uploadBoard(APIView):
    def get(self, request):
        userID = str(request.GET.get("userName", None))
        boardName = str(request.GET.get("boardName", None))
        boardScene = str(request.GET.get("boardScene", None))
        boardTime = str(request.GET.get("boardTime", None))
        boardIntroduction = str(request.GET.get("boardIntroduction", None))
        # boardData = request.FILES.get('file')
        res = Doctor.objects.get(id=userID)
        userName = res.name
        boardNum = RecordTemplate.objects.all().count()
        board = RecordTemplate(
            id=boardNum + 1,
            name=boardName,
            ownerID=userID,
            ownerName=userName,
            time=boardTime,
            scene=boardScene,
            description=boardIntroduction,
        )
        board.save()
        return Response(0)


class deleteBoard(APIView):
    def get(self, request):
        id = str(request.GET.get("boardID", None))
        board = RecordTemplate.objects.get(id=id)
        board.delete()
        return Response(0)


class getDoctorDiagnosisTaskList(APIView):
    def get(self, request):
        res = DiagnosisMission.objects.all()
        ans = []
        for i in res:
            ans.append(
                {
                    "id": i.id,
                    "name": i.name,
                    "patientID": i.patient_id_id,
                    "patientName": i.patient_name,
                    "finishState": i.state,
                    "notifyResultState": True if i.whetherPublic == '是' else False,
                    "time": i.startTime,
                    "endTime": i.endTime,
                    "introduction": i.description,
                    "scene": i.scene,
                    "data": i.data,
                    "model": i.model,
                    "resultDisease": i.resultDisease,
                    "resultStage": i.resultStage,
                }
            )
        return Response(ans)


class DoctorEstablishDiagnosisTask(APIView):
    def get(self, request):
        taskName = str(request.GET.get("taskName", None))
        taskIntroduction = str(request.GET.get("taskIntroduction", None))
        taskScene = str(request.GET.get("taskScene", None))
        patientID = str(request.GET.get("patientID", None))
        taskData = "默认数据集"
        taskModel = "默认模型"
        taskState = "已完成"
        taskNotifyState = "否"
        taskStartTime = datetime.datetime.now()
        taskNum = DiagnosisMission.objects.all().count()
        res = Public.objects.get(id=patientID)
        patientName = res.name
        task = DiagnosisMission(
            id=taskNum + 1,
            name=taskName,
            patient_id_id=patientID,
            patient_name=patientName,
            researcherEstablish="否",
            whetherPublic=taskNotifyState,
            startTime=taskStartTime,
            description=taskIntroduction,
            state=taskState,
            data=taskData,
            model=taskModel,
            scene=taskScene,
        )
        task.save()
        return Response(0)


class DeleteDiagnosisTask(APIView):
    def get(self, request):
        taskID = str(request.GET.get("taskID", None))
        task = DiagnosisMission.objects.get(id=taskID)
        task.delete()
        return Response(0)


class updateAssistantNotifyState(APIView):
    def get(self, request):
        taskID = str(request.GET.get("taskID", None))
        notifyResultState = str(request.GET.get("notifyResultState", None))
        task = DiagnosisMission.objects.get(id=taskID)
        task.whetherPublic = notifyResultState
        task.save()
        print(task.whetherPublic)
        return Response(0)


class saveEditAssistanceResult(APIView):
    def get(self, request):
        taskID = str(request.GET.get("taskID", None))
        resultDisease = str(request.GET.get("resultDisease", None))
        resultStage = str(request.GET.get("resultStage", None))
        task = DiagnosisMission.objects.get(id=taskID)
        task.resultDisease = resultDisease
        task.resultStage = resultStage
        task.save()
        return Response(0)


class getDoctorPredictTaskList(APIView):
    def get(self, request):
        res = PredictMission.objects.all()
        ans = []
        for i in res:
            ans.append(
                {
                    "id": i.id,
                    "name": i.name,
                    "finishState": i.state,
                    "patientID": i.patient_id_id,
                    "patientName": i.patient_name,
                    "notifyPredictState": True if i.whetherPublic == '是' else False,
                    "time": i.startTime,
                    "endTime": i.endTime,
                    "introduction": i.description,
                    "scene": i.scene,
                    "data": i.data,
                    "model": i.model,
                    "risk": i.risk,
                }
            )
        return Response(ans)


class DoctorEstablishPredictTask(APIView):
    def get(self, request):
        taskName = str(request.GET.get("taskName", None))
        taskIntroduction = str(request.GET.get("taskIntroduction", None))
        patientID = str(request.GET.get("patientID", None))
        taskScene = str(request.GET.get("taskScene", None))
        print(taskScene)
        taskDataset = str(request.GET.get("taskDataset", None))
        taskModel = str(request.GET.get("taskModel", None))
        taskNotifyState = "否"
        taskStartTime = datetime.datetime.now()
        taskState = "已完成"
        taskNum = PredictMission.objects.all().count()
        res = Public.objects.get(id=patientID)
        patientName = res.name
        task = PredictMission(
            id=taskNum + 1,
            name=taskName,
            patient_id_id=patientID,
            patient_name=patientName,
            researcherEstablish="否",
            whetherPublic=taskNotifyState,
            startTime=taskStartTime,
            endTime=taskStartTime,
            state=taskState,
            description=taskIntroduction,
            data=taskDataset,
            model=taskModel,
            scene=taskScene
        )
        task.save()
        return Response(0)


class updatePredictState(APIView):
    def get(self, request):
        taskID = str(request.GET.get("taskID", None))
        notifyPredictState = str(request.GET.get("notifyPredictState", None))
        task = PredictMission.objects.get(id=taskID)
        task.whetherPublic = notifyPredictState
        task.save()
        return Response(0)


class DeletePredictTask(APIView):
    def get(self, request):
        taskID = str(request.GET.get("taskID", None))
        task = PredictMission.objects.get(id=taskID)
        task.delete()
        return Response(0)


class getRecommendationTaskList(APIView):
    def get(self, request):
        res = PlanRecommendMission.objects.all()
        ans = []
        for i in res:
            ans.append(
                {
                    "id": i.id,
                    "name": i.name,
                    "finishState": i.state,
                    "notifySchemeState": True if i.whetherPublic == '是' else False,
                    "time": i.startTime,
                    "introduction": i.description,
                    "scene": i.scene,
                    "patientID": i.patient_id_id,
                    "patientName": i.patient_name,
                    "recommendation": i.plan,
                }
            )
        return Response(ans)


class updateScheme(APIView):
    def get(self, request):
        taskID = str(request.GET.get("taskID", None))
        scheme = str(request.GET.get("scheme", None))
        task = PlanRecommendMission.objects.get(id=taskID)
        task.plan = scheme
        task.save()
        return Response(0)


class updateSchemeState(APIView):
    def get(self, request):
        taskID = str(request.GET.get("taskID", None))
        notifySchemeState = str(request.GET.get("notifySchemeState", None))
        task = PlanRecommendMission.objects.get(id=taskID)
        task.whetherPublic = notifySchemeState
        task.save()
        return Response(0)


class DeleteRecommendationTask(APIView):
    def get(self, request):
        taskID = str(request.GET.get("taskID", None))
        task = PlanRecommendMission.objects.get(id=taskID)
        task.delete()
        return Response(0)


class DoctorEstablishSchemeTask(APIView):
    def get(self, request):
        taskName = str(request.GET.get("taskName", None))
        taskIntroduction = str(request.GET.get("taskIntroduction", None))
        taskScene = str(request.GET.get("taskScene", None))
        patientID = str(request.GET.get("patientID", None))
        taskNotifyState = "否"
        taskStartTime = datetime.datetime.now()
        taskState = "已完成"
        taskDataset = str(request.GET.get("taskDataset", None))
        taskModel = str(request.GET.get("taskModel", None))
        taskNum = PlanRecommendMission.objects.all().count()
        res = Public.objects.get(id=patientID)
        patientName = res.name
        plan = str(request.GET.get("taskPlan", None))
        task = PlanRecommendMission(
            id=taskNum + 1,
            name=taskName,
            patient_id_id=patientID,
            patient_name=patientName,
            researcherEstablish="否",
            whetherPublic=taskNotifyState,
            startTime=taskStartTime,
            state=taskState,
            description=taskIntroduction,
            data=taskDataset,
            model=taskModel,
            scene=taskScene,
        )
        task.plan = plan + '<br>' +  task.plan
        task.save()
        return Response(0)


class uploadModel(APIView):
    def get(self, request):
        name = str(request.GET.get("name", None))
        introduction = str(request.GET.get("introduction", None))
        scene = str(request.GET.get("scene", None))
        type = str(request.GET.get("type", None))
        data = str(request.GET.get("data", None))
        modelNum = BigModel.objects.all().count()
        # modelLoad = request.FILES.get('file')
        ownerID = str(request.GET.get("ownerID", None))
        ownerName = str(request.GET.get("ownerName", None))
        bigmodel = BigModel(
            id=modelNum + 1,
            name=name,
            scene=scene,
            description=introduction,
            ownerID=ownerID,
            ownerName=ownerName,
            type=type,
            data=data,
            time=datetime.datetime.now(),
        )
        bigmodel.save()
        return Response(0)


class getModleList(APIView):
    def get(self, request):
        res = BigModel.objects.all()
        ans = []
        for i in res:
            ans.append(
                {
                    "id": i.id,
                    "name": i.name,
                    "type": i.type,
                    "ownerID": i.ownerID,
                    "ownerName": i.ownerName,
                    "time": i.time,
                    "scenes": i.scene,
                    "data": i.data,
                    "introduction": i.description,
                }
            )
        return Response(ans)


class deleteModel(APIView):
    def get(self, request):
        id = str(request.GET.get("modelID", None))
        model = BigModel.objects.get(id=id)
        model.delete()
        return Response(0)


class getScientistDignosisTaskList(APIView):
    def get(self, request):
        res = DiagnosisMission.objects.all()
        ans = []
        for i in res:
            if i.researcherEstablish == "是":
                ans.append(
                    {
                        "id": i.id,
                        "name": i.name,
                        "patientID": i.patient_id_id,
                        "patientName": i.patient_name,
                        "finishState": i.state,
                        "notifyResultState": i.whetherPublic,
                        "time": i.startTime,
                        "endTime": i.endTime,
                        "introduction": i.description,
                        "scene": i.scene,
                        "data": i.data,
                        "model": i.model,
                        "MAE_MMSE": "2.1373 ± 0.0442",
                        "MAE_CDRG": "0.2753 ± 0.0029",
                        "MAE_CDRS": "1.3560 ± 0.0190",
                        "MAE_ADAS": "5.8689 ± 0.0623",
                        "wR_MMSE": "0.7620 ± 0.0132",
                        "wR_CDRG": "0.7415 ± 0.0050",
                        "wR_CDRS": "0.7979 ± 0.0083",
                        "wR_ADAS": "0.7249 ± 0.0165",
                    }
                )
        return Response(ans)


class establishScientistDiagnosisTask(APIView):
    def get(self, request):
        taskName = str(request.GET.get("taskName", None))
        taskIntroduction = str(request.GET.get("taskIntroduction", None))
        taskScene = str(request.GET.get("taskScene", None))
        patientID = '21370123'
        taskData = str(request.GET.get("taskDataset", None))
        taskModel = str(request.GET.get("taskModel", None))
        taskState = "未完成"
        taskNotifyState = "否"
        taskStartTime = datetime.datetime.now()
        taskNum = DiagnosisMission.objects.all().count()
        res = Public.objects.get(id=patientID)
        patientName = res.name
        task = DiagnosisMission(
            id=taskNum + 1,
            name=taskName,
            patient_id_id=patientID,
            patient_name=patientName,
            researcherEstablish="是",
            whetherPublic=taskNotifyState,
            startTime=taskStartTime,
            description=taskIntroduction,
            state=taskState,
            data=taskData,
            model=taskModel,
            scene=taskScene,
        )
        task.save()
        return Response(0)


class DeleteScientistDiagnosisTask(APIView):
    def get(self, request):
        taskID = str(request.GET.get("taskID", None))
        task = DiagnosisMission.objects.get(id=taskID)
        task.delete()
        return Response(0)


class getScientistPredictTaskList(APIView):
    def get(self, request):
        res = PredictMission.objects.all()
        ans = []
        for i in res:
            if i.researcherEstablish == "是":
                ans.append(
                    {
                        "id": i.id,
                        "name": i.name,
                        "finishState": i.state,
                        "time": i.startTime,
                        "endTime": i.endTime,
                        "introduction": i.description,
                        "scene": i.scene,
                        "data": i.data,
                        "model": i.model,
                        "risk": i.risk,
                    }
                )
        return Response(ans)


class ScientistEstablishPredictTask(APIView):
    def get(self, request):
        taskName = str(request.GET.get("taskName", None))
        taskIntroduction = str(request.GET.get("taskIntroduction", None))
        patientID = patientID = '21370123'
        taskScene = str(request.GET.get("taskScene", None))
        taskDataset = str(request.GET.get("taskDataset", None))
        taskModel = str(request.GET.get("taskModel", None))
        taskNotifyState = "否"
        taskStartTime = datetime.datetime.now()
        taskState = "未完成"
        taskNum = PredictMission.objects.all().count()
        res = Public.objects.get(id=patientID)
        patientName = res.name
        task = PredictMission(
            id=taskNum + 1,
            name=taskName,
            patient_id_id=patientID,
            patient_name=patientName,
            researcherEstablish="是",
            whetherPublic=taskNotifyState,
            startTime=taskStartTime,
            state=taskState,
            description=taskIntroduction,
            data=taskDataset,
            model=taskModel,
            risk="",
            scene=taskScene,
        )
        task.save()
        return Response(0)


class DeleteScientistPredictTask(APIView):
    def get(self, request):
        taskID = str(request.GET.get("taskID", None))
        task = PredictMission.objects.get(id=taskID)
        task.delete()
        return Response(0)


class getScientistRecommendationTaskList(APIView):
    def get(self, request):
        res = PlanRecommendMission.objects.all()
        ans = []
        for i in res:
            if i.researcherEstablish == "是":
                ans.append(
                    {
                        "id": i.id,
                        "name": i.name,
                        "finishState": i.state,
                        "time": i.startTime,
                        "introduction": i.description,
                        "scene": i.scene,
                        "data": i.data,
                        "model": i.model,
                        "recommendation": i.plan,
                    }
                )
        return Response(ans)


class ScientistEstablishSchemeTask(APIView):
    def get(self, request):
        taskName = str(request.GET.get("taskName", None))
        taskIntroduction = str(request.GET.get("taskIntroduction", None))
        taskScene = str(request.GET.get("taskScene", None))
        patientID = patientID = '21370123'
        taskNotifyState = "否"
        taskStartTime = datetime.datetime.now()
        taskState = "未完成"
        taskDataset = str(request.GET.get("taskDataset", None))
        taskModel = str(request.GET.get("taskModel", None))
        taskNum = PlanRecommendMission.objects.all().count()
        res = Public.objects.get(id=patientID)
        patientName = res.name
        task = PlanRecommendMission(
            id=taskNum + 1,
            name=taskName,
            patient_id_id=patientID,
            patient_name=patientName,
            researcherEstablish="是",
            whetherPublic=taskNotifyState,
            startTime=taskStartTime,
            state=taskState,
            description=taskIntroduction,
            data=taskDataset,
            model=taskModel,
            plan="",
            scene=taskScene,
        )
        task.save()
        return Response(0)
