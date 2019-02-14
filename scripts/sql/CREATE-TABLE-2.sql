USE [HealthcareDB]
GO

/****** Object:  Table [dbo].[Patient]    Script Date: 2/14/2019 5:41:59 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Patient](
	[Id] [int] NULL,
	[Name] [varchar](100) NULL,
	[PhoneNumber] [varchar](100) NULL,
	[Address] [varchar](100) NULL,
	[City] [varchar](100) NULL,
	[BirthDate] [varchar](20) NULL,
	[Height] [int] NULL,
	[Weight] [int] NULL
) ON [PRIMARY]
GO


