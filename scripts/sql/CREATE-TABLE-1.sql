USE [HealthcareDB]
GO

/****** Object:  Table [dbo].[HealthcareData]    Script Date: 2/14/2019 5:38:23 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[HealthcareData](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[time] [datetime] NULL,
	[PatientId] [int] NULL,
	[SystolicBloodPressure] [int] NULL,
	[DiastolicBloodPressure] [int] NULL,
	[HeartRate] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO


