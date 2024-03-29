# Generated by Django 4.2.5 on 2024-03-18 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Researcher",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="研究员账号",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="研究员姓名")),
                ("password", models.CharField(max_length=255, verbose_name="研究员密码")),
                ("department", models.CharField(max_length=255, verbose_name="所属单位")),
            ],
            options={
                "db_table": "researcher",
                "indexes": [
                    models.Index(fields=["id"], name="researcher_id_32ef2c_idx")
                ],
            },
        ),
        migrations.CreateModel(
            name="RecordTemplate",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="模板编号",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="模板名称"
                    ),
                ),
                (
                    "ownerID",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="模板所有者"
                    ),
                ),
                (
                    "ownerName",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="模板所有者姓名"
                    ),
                ),
                (
                    "time",
                    models.DateTimeField(blank=True, null=True, verbose_name="模板上传时间"),
                ),
                (
                    "scene",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="模板应用场景"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="模板描述"),
                ),
                (
                    "data",
                    models.FileField(
                        blank=True, null=True, upload_to="", verbose_name="模板文件"
                    ),
                ),
            ],
            options={
                "db_table": "record_template",
                "indexes": [
                    models.Index(fields=["id"], name="record_temp_id_28237d_idx")
                ],
            },
        ),
        migrations.CreateModel(
            name="Public",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="用户账号",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="用户姓名")),
                ("password", models.CharField(max_length=255, verbose_name="用户密码")),
                ("gender", models.CharField(max_length=10, verbose_name="用户性别")),
                ("age", models.IntegerField(verbose_name="用户年龄")),
                ("birthdate", models.DateField(null=True, verbose_name="用户生日")),
                ("region", models.CharField(max_length=255, verbose_name="用户住址")),
                ("education", models.CharField(max_length=255, verbose_name="用户学历")),
                ("phone", models.CharField(max_length=255, verbose_name="用户电话")),
                ("identy", models.CharField(max_length=255, verbose_name="用户电话")),
                ("ApoE", models.FloatField(verbose_name="ApoE")),
                ("MMSE", models.FloatField(verbose_name="MMSE")),
                ("CDR_Global", models.FloatField(verbose_name="CDR_Global")),
                ("CDR_SOB", models.FloatField(verbose_name="CDR_SOB")),
                ("ADAS_Cog", models.FloatField(verbose_name="ADAS_Cog")),
                ("MRI", models.FloatField(verbose_name="MRI")),
                ("PET", models.FloatField(verbose_name="PET")),
            ],
            options={
                "db_table": "public",
                "indexes": [models.Index(fields=["id"], name="public_id_0f9404_idx")],
            },
        ),
        migrations.CreateModel(
            name="Model",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="模型编号",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="模型名称")),
                ("type", models.CharField(max_length=255, verbose_name="模型类型")),
                ("ownerID", models.CharField(max_length=50, verbose_name="模型所有者")),
                ("ownerName", models.CharField(max_length=255, verbose_name="模型所有者姓名")),
                ("time", models.DateTimeField(verbose_name="模型上传时间")),
                ("scene", models.CharField(max_length=255, verbose_name="模型应用场景")),
                ("data", models.CharField(max_length=255, verbose_name="模型数据集")),
                (
                    "model",
                    models.FileField(
                        blank=True, null=True, upload_to="", verbose_name="模型文件"
                    ),
                ),
                ("description", models.TextField(verbose_name="模型描述")),
            ],
            options={
                "db_table": "model",
                "indexes": [models.Index(fields=["id"], name="model_id_2ffab6_idx")],
            },
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="医生账号",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="医生姓名")),
                ("password", models.CharField(max_length=255, verbose_name="医生密码")),
                ("hospital", models.CharField(max_length=255, verbose_name="所属医院")),
                ("department", models.CharField(max_length=255, verbose_name="所属部门")),
            ],
            options={
                "db_table": "doctor",
                "indexes": [models.Index(fields=["id"], name="doctor_id_ecf006_idx")],
            },
        ),
        migrations.CreateModel(
            name="Data",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="数据集编号",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="数据集名称")),
                ("ownerID", models.CharField(max_length=50, verbose_name="数据集所有者")),
                (
                    "ownerName",
                    models.CharField(max_length=255, verbose_name="数据集所有者姓名"),
                ),
                ("time", models.DateTimeField(verbose_name="数据集上传时间")),
                ("size", models.FloatField(verbose_name="数据集大小")),
                ("scene", models.CharField(max_length=255, verbose_name="数据集应用场景")),
                ("description", models.CharField(max_length=255, verbose_name="数据集描述")),
                ("model", models.CharField(max_length=255, verbose_name="数据集关联模型")),
                (
                    "data",
                    models.FileField(
                        blank=True, null=True, upload_to="", verbose_name="数据集文件"
                    ),
                ),
            ],
            options={
                "db_table": "data",
                "indexes": [models.Index(fields=["id"], name="data_id_aec06e_idx")],
            },
        ),
        migrations.CreateModel(
            name="PredictMission",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="任务编号",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="任务名称")),
                ("patient_name", models.CharField(max_length=255, verbose_name="患者姓名")),
                (
                    "researcherEstablish",
                    models.CharField(max_length=10, verbose_name="是否为科研人员创建"),
                ),
                (
                    "whetherPublic",
                    models.CharField(max_length=10, verbose_name="是否通知病人"),
                ),
                ("startTime", models.DateField(verbose_name="任务开始时间")),
                ("endTime", models.DateField(verbose_name="任务结束时间")),
                ("data", models.CharField(max_length=255, verbose_name="任务数据集")),
                ("model", models.CharField(max_length=255, verbose_name="任务模型")),
                ("scene", models.CharField(max_length=255, verbose_name="任务应用场景")),
                ("risk", models.CharField(max_length=255, verbose_name="风险预测")),
                ("description", models.CharField(max_length=255, verbose_name="任务描述")),
                ("state", models.CharField(max_length=255, verbose_name="任务状态")),
                (
                    "patient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.public"
                    ),
                ),
            ],
            options={
                "db_table": "predict_mission",
                "indexes": [
                    models.Index(fields=["id"], name="predict_mis_id_ecda9c_idx")
                ],
            },
        ),
        migrations.CreateModel(
            name="PlanRecommendMission",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="任务编号",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="任务名称")),
                (
                    "patient_name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="患者姓名"
                    ),
                ),
                (
                    "researcherEstablish",
                    models.CharField(max_length=10, verbose_name="是否为科研人员创建"),
                ),
                (
                    "whetherPublic",
                    models.CharField(max_length=10, verbose_name="是否通知病人"),
                ),
                ("startTime", models.DateField(verbose_name="任务开始时间")),
                ("endTime", models.DateField(verbose_name="任务结束时间")),
                ("data", models.CharField(max_length=255, verbose_name="任务数据集")),
                ("model", models.CharField(max_length=255, verbose_name="任务模型")),
                ("scene", models.CharField(max_length=255, verbose_name="任务应用场景")),
                ("plan", models.TextField(blank=True, null=True, verbose_name="干预方案")),
                ("state", models.CharField(max_length=255, verbose_name="任务状态")),
                (
                    "patient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.public"
                    ),
                ),
            ],
            options={
                "db_table": "plan_recommend_mission",
                "indexes": [
                    models.Index(fields=["id"], name="plan_recomm_id_6b4db9_idx")
                ],
            },
        ),
        migrations.CreateModel(
            name="DiagnosisMission",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="任务编号",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="任务名称")),
                (
                    "patient_name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="患者姓名"
                    ),
                ),
                (
                    "researcherEstablish",
                    models.CharField(max_length=10, verbose_name="是否为科研人员创建"),
                ),
                (
                    "whetherPublic",
                    models.CharField(max_length=10, verbose_name="是否通知病人"),
                ),
                ("startTime", models.DateField(verbose_name="任务开始时间")),
                ("endTime", models.DateField(verbose_name="任务结束时间")),
                ("description", models.CharField(max_length=255, verbose_name="任务描述")),
                ("data", models.CharField(max_length=255, verbose_name="任务数据集")),
                ("model", models.CharField(max_length=255, verbose_name="任务模型")),
                ("scene", models.CharField(max_length=255, verbose_name="任务应用场景")),
                (
                    "resultDisease",
                    models.CharField(max_length=255, verbose_name="任务结果"),
                ),
                (
                    "resultStage",
                    models.CharField(max_length=255, verbose_name="任务应用场景"),
                ),
                ("state", models.CharField(max_length=255, verbose_name="任务状态")),
                (
                    "MAE_MMSE",
                    models.CharField(
                        default="2.1373 ± 0.0442",
                        max_length=50,
                        verbose_name="MAE_MMSE得分",
                    ),
                ),
                (
                    "MAE_CDRG",
                    models.CharField(
                        default="0.2753 ± 0.0029",
                        max_length=50,
                        verbose_name="MAE_CDRG得分",
                    ),
                ),
                (
                    "MAE_CDRS",
                    models.CharField(
                        default="1.3560 ± 0.0190",
                        max_length=50,
                        verbose_name="MAE_CDRS得分",
                    ),
                ),
                (
                    "MAE_ADAS",
                    models.CharField(
                        default="5.8689 ± 0.0623",
                        max_length=50,
                        verbose_name="MAE_ADAS得分",
                    ),
                ),
                (
                    "wR_MMSE",
                    models.CharField(
                        default="0.7620 ± 0.0132",
                        max_length=50,
                        verbose_name="wR_MMSE得分",
                    ),
                ),
                (
                    "wR_CDRG",
                    models.CharField(
                        default="0.7415 ± 0.0050",
                        max_length=50,
                        verbose_name="wR_CDRG得分",
                    ),
                ),
                (
                    "wR_CDRS",
                    models.CharField(
                        default="0.7979 ± 0.0083",
                        max_length=50,
                        verbose_name="wR_CDRS得分",
                    ),
                ),
                (
                    "wR_ADAS",
                    models.CharField(
                        default="0.7249 ± 0.0165",
                        max_length=50,
                        verbose_name="wR_ADAS得分",
                    ),
                ),
                (
                    "patient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.public"
                    ),
                ),
            ],
            options={
                "db_table": "diagnosis_mission",
                "indexes": [
                    models.Index(fields=["id"], name="diagnosis_m_id_4d9a71_idx")
                ],
            },
        ),
    ]
