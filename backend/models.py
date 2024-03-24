from django.db import models


class Public(models.Model):
    id = models.CharField(verbose_name="用户账号", max_length=50, primary_key=True)
    name = models.CharField(verbose_name="用户姓名", max_length=255, null=True, blank=True)
    password = models.CharField(verbose_name="用户密码", max_length=255, null=True, blank=True)
    gender = models.CharField(verbose_name="用户性别", max_length=10, null=True, blank=True)
    # SchemeState = models.CharField(verbose_name="是否允许方案查看", max_length=10, null=True, blank=True, default='否')
    # recommendation = models.CharField(verbose_name="推荐方案", max_length=10, null=True, blank=True, default='否')
    age = models.CharField(verbose_name="用户年龄", max_length=50, null=True, blank=True)
    birthdate = models.CharField(verbose_name="用户生日", max_length=50, null=True, blank=True)
    region = models.CharField(verbose_name="用户住址", max_length=255, null=True, blank=True)
    history = models.CharField(verbose_name="用户病史", max_length=255, null=True, blank=True)
    education = models.CharField(verbose_name="用户学历", max_length=255, null=True, blank=True)
    phone = models.CharField(verbose_name="用户电话", max_length=255, null=True, blank=True)
    identy = models.CharField(verbose_name="身份证号", max_length=255, null=True, blank=True)
    ApoE = models.CharField(verbose_name="ApoE", max_length=50,null=True, blank=True)
    MMSE = models.CharField(verbose_name="MMSE", max_length=50,null=True, blank=True)
    CDR_Global = models.CharField(verbose_name="CDR_Global", max_length=50,null=True, blank=True)
    CDR_SOB = models.CharField(verbose_name="CDR_SOB", max_length=50,null=True, blank=True)
    ADAS_Cog = models.CharField(verbose_name="ADAS_Cog", max_length=50,null=True, blank=True)
    MRI = models.CharField(verbose_name="MRI", max_length=50,null=True, blank=True)
    PET = models.CharField(verbose_name="PET", max_length=50,null=True, blank=True)

    class Meta:
        db_table = "public"
        indexes = [models.Index(fields=["id"])]


class Doctor(models.Model):
    id = models.CharField(verbose_name="医生账号", max_length=50, primary_key=True)
    name = models.CharField(verbose_name="医生姓名", max_length=255)
    password = models.CharField(verbose_name="医生密码", max_length=255)
    hospital = models.CharField(verbose_name="所属医院", max_length=255, null=True, blank=True)
    department = models.CharField(verbose_name="所属部门", max_length=255, null=True, blank=True)

    class Meta:
        db_table = "doctor"
        indexes = [models.Index(fields=["id"])]


class Researcher(models.Model):
    id = models.CharField(verbose_name="研究员账号", max_length=50, primary_key=True)
    name = models.CharField(verbose_name="研究员姓名", max_length=255)
    password = models.CharField(verbose_name="研究员密码", max_length=255)
    department = models.CharField(verbose_name="所属单位", max_length=255, null=True, blank=True)

    class Meta:
        db_table = "researcher"
        indexes = [models.Index(fields=["id"])]


class BigModel(models.Model):
    id = models.CharField(verbose_name="模型编号", max_length=50, primary_key=True)
    name = models.CharField(verbose_name="模型名称", max_length=255, null=True, blank=True)
    type = models.CharField(verbose_name="模型类型", max_length=255, null=True, blank=True)
    ownerID = models.CharField(verbose_name="模型所有者", max_length=50, null=True, blank=True)
    ownerName = models.CharField(verbose_name="模型所有者姓名", max_length=255, null=True, blank=True)
    time = models.DateTimeField(verbose_name="模型上传时间", null=True, blank=True)
    scene = models.CharField(verbose_name="模型应用场景", max_length=255, null=True, blank=True)
    data = models.CharField(verbose_name="模型数据集", max_length=255, null=True, blank=True)
    model = models.FileField(verbose_name="模型文件", blank=True, null=True)
    description = models.TextField(verbose_name="模型描述", null=True, blank=True)

    class Meta:
        db_table = "BigModel"
        indexes = [models.Index(fields=["id"])]


class Data(models.Model):
    id = models.CharField(verbose_name="数据集编号", max_length=50, primary_key=True)
    name = models.CharField(verbose_name="数据集名称", max_length=255, null=True, blank=True)
    ownerID = models.CharField(verbose_name="数据集所有者", max_length=50, null=True, blank=True)
    ownerName = models.CharField(verbose_name="数据集所有者姓名", max_length=255, null=True, blank=True)
    time = models.CharField(verbose_name="数据集上传时间",  max_length=50, null=True, blank=True)
    size = models.CharField(verbose_name="数据集大小", max_length=50, null=True, blank=True)
    scene = models.CharField(verbose_name="数据集应用场景", max_length=255, null=True, blank=True)
    description = models.CharField(verbose_name="数据集描述", max_length=255, null=True, blank=True)
    model = models.CharField(verbose_name="数据集关联模型", max_length=255, null=True, blank=True)
    data = models.FileField(verbose_name="数据集文件", null=True, blank=True)

    class Meta:
        db_table = "data"
        indexes = [models.Index(fields=["id"])]


class RecordTemplate(models.Model):
    id = models.CharField(verbose_name="模板编号", max_length=50, primary_key=True)
    name = models.CharField(verbose_name="模板名称", max_length=255, null=True, blank=True)
    ownerID = models.CharField(verbose_name="模板所有者", max_length=50, null=True, blank=True)
    ownerName = models.CharField(verbose_name="模板所有者姓名", max_length=255, null=True, blank=True)
    time = models.DateTimeField(verbose_name="模板上传时间", null=True, blank=True)
    scene = models.CharField(verbose_name="模板应用场景", max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name="模板描述", null=True, blank=True)
    data = models.FileField(verbose_name="模板文件", null=True, blank=True)

    class Meta:
        db_table = "record_template"
        indexes = [models.Index(fields=["id"])]


class DiagnosisMission(models.Model):
    id = models.CharField(verbose_name="任务编号", max_length=50, primary_key=True)
    name = models.CharField(verbose_name="任务名称", max_length=255)
    patient_id = models.ForeignKey(
        Public, on_delete=models.CASCADE,
    )
    patient_name = models.CharField(verbose_name="患者姓名", max_length=255, null=True, blank=True)
    researcherEstablish = models.CharField(verbose_name="是否为科研人员创建", max_length=10, null=True, blank=True)
    whetherPublic = models.CharField(verbose_name="是否通知病人", max_length=10, null=True, blank=True)
    startTime = models.CharField(verbose_name="任务开始时间", max_length=50, null=True, blank=True)
    endTime = models.CharField(verbose_name="任务结束时间", max_length=50, null=True, blank=True)
    description = models.CharField(verbose_name="任务描述", max_length=255, null=True, blank=True)
    data = models.CharField( verbose_name="任务数据集", max_length=255, null=True, blank=True)
    model = models.CharField( verbose_name="任务模型", max_length=255, null=True, blank=True)
    scene = models.CharField(verbose_name="任务应用场景", max_length=255, null=True, blank=True)
    resultDisease = models.CharField(verbose_name="任务结果", max_length=255, null=True, blank=True, default='阿尔兹海默症')
    resultStage = models.CharField(verbose_name="任务应用场景", max_length=255, null=True, blank=True, default='初期')
    state = models.CharField(verbose_name="任务状态", max_length=255, null=True, blank=True)
    MAE_MMSE = models.CharField(
        max_length=50, verbose_name="MAE_MMSE得分", default="2.1373 ± 0.0442"
    )
    MAE_CDRG = models.CharField(
        max_length=50, verbose_name="MAE_CDRG得分", default="0.2753 ± 0.0029"
    )
    MAE_CDRS = models.CharField(
        max_length=50, verbose_name="MAE_CDRS得分", default="1.3560 ± 0.0190"
    )
    MAE_ADAS = models.CharField(
        max_length=50, verbose_name="MAE_ADAS得分", default="5.8689 ± 0.0623"
    )
    wR_MMSE = models.CharField(
        max_length=50, verbose_name="wR_MMSE得分", default="0.7620 ± 0.0132"
    )
    wR_CDRG = models.CharField(
        max_length=50, verbose_name="wR_CDRG得分", default="0.7415 ± 0.0050"
    )
    wR_CDRS = models.CharField(
        max_length=50, verbose_name="wR_CDRS得分", default="0.7979 ± 0.0083"
    )
    wR_ADAS = models.CharField(
        max_length=50, verbose_name="wR_ADAS得分", default="0.7249 ± 0.0165"
    )

    class Meta:
        db_table = "diagnosis_mission"
        indexes = [models.Index(fields=["id"])]


class PredictMission(models.Model):
    id = models.CharField(verbose_name="任务编号", max_length=50, primary_key=True)
    name = models.CharField(verbose_name="任务名称", max_length=255)
    patient_id = models.ForeignKey(
        Public, on_delete=models.SET_NULL, null=True, blank=True
    )
    patient_name = models.CharField(verbose_name="患者姓名", max_length=255, null=True, blank=True)
    researcherEstablish = models.CharField(verbose_name="是否为科研人员创建", max_length=10, null=True, blank=True)
    whetherPublic = models.CharField(verbose_name="是否通知病人", max_length=10, null=True, blank=True)
    startTime = models.CharField(verbose_name="任务开始时间", max_length=50, null=True, blank=True)
    endTime = models.CharField(verbose_name="任务结束时间", max_length=50, null=True, blank=True)
    data = models.CharField(verbose_name="任务数据集", max_length=255, null=True, blank=True)
    model = models.CharField(verbose_name="任务模型", max_length=255, null=True, blank=True)
    scene = models.CharField(verbose_name="任务应用场景", max_length=255, null=True, blank=True)
    risk = models.CharField(verbose_name="风险预测", max_length=255, null=True, blank=True, default='有一定几率发展为中期')
    description = models.CharField(verbose_name="任务描述", max_length=255, null=True, blank=True)
    state = models.CharField(verbose_name="任务状态", max_length=255, null=True, blank=True)

    class Meta:
        db_table = "predict_mission"
        indexes = [models.Index(fields=["id"])]


class PlanRecommendMission(models.Model):
    id = models.CharField(verbose_name="任务编号", max_length=50, primary_key=True)
    name = models.CharField(verbose_name="任务名称", max_length=255)
    patient_id = models.ForeignKey(Public, on_delete=models.SET_NULL, null=True, blank=True)
    patient_name = models.CharField(verbose_name="患者姓名", max_length=255,  null=True, blank=True)
    researcherEstablish = models.CharField(verbose_name="是否为科研人员创建", max_length=10, null=True, blank=True)
    whetherPublic = models.CharField(verbose_name="是否通知病人", max_length=10, null=True, blank=True)
    startTime = models.CharField(verbose_name="任务开始时间", max_length=50, null=True, blank=True)
    endTime = models.CharField(verbose_name="任务结束时间", max_length=50, null=True, blank=True)
    data = models.CharField(verbose_name="任务数据集", max_length=255, null=True, blank=True)
    model = models.CharField(verbose_name="任务模型", max_length=255, null=True, blank=True)
    scene = models.CharField(verbose_name="任务应用场景", max_length=255, null=True, blank=True)
    plan = models.TextField(verbose_name="干预方案", null=True, blank=True, default='<div>家人应该持续陪伴，做好患者的清洁卫生工作，关注情绪，注意保暖。<br><br><strong>药物治疗：</strong><br>胆碱酯酶抑制剂（Cholinesterase Inhibitors）： 这类药物包括多巴胺胆碱酯酶抑制剂（如多奈哌齐）、甲氧氯普胺和依非酰胆碱酯酶抑制剂。它们可用于改善大脑中的神经递质水平，帮助提高认知功能和日常生活能力。<br>NMDA受体拮抗剂： 如美金刚、拉美西头孢等，可用于中度至重度阿尔兹海默症患者，帮助缓解症状和减缓疾病进展。<br><br><strong>非药物治疗：</strong><br>认知训练和康复： 包括记忆训练、注意力练习和问题解决技能训练等，旨在帮助患者维持或提高日常生活功能。<br>生活方式干预： 促进健康的生活方式，包括规律的锻炼、健康饮食、充足睡眠等，有助于改善患者的整体健康状况。<br>情绪支持和心理疏导： 提供情绪支持和心理疏导服务，帮助患者和家人应对情绪上的困扰和应对挑战。<br><br><strong>支持性护理：</strong><br>日常生活支持： 提供日常生活活动的帮助，如饮食、洗漱、穿衣等，以维持患者的基本生活功能。<br>社交支持： 通过参加社交活动和与家人、朋友以及社区联系，提供社交支持和心理支持。<br>安全保障： 确保患者生活在安全的环境中，防止意外和伤害发生，如安装防跌倒设备、监控用具等。</div>')
    state = models.CharField(verbose_name="任务状态", max_length=255, null=True, blank=True)
    description = models.CharField(verbose_name="任务描述", max_length=255, null=True, blank=True)

    class Meta:
        db_table = "plan_recommend_mission"
        indexes = [models.Index(fields=["id"])]
