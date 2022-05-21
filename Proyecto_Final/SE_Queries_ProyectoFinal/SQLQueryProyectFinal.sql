USE [master];

GO
DROP DATABASE [DB_API_RESTful_ProyectFinal];

GO
/*****	CREATE DATABASE	******/
CREATE DATABASE [DB_API_RESTful_ProyectFinal];

GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET ARITHABORT OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET  DISABLE_BROKER 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET RECOVERY FULL 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET  MULTI_USER 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET DB_CHAINING OFF 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET DELAYED_DURABILITY = DISABLED 
GO
EXEC sys.sp_db_vardecimal_storage_format N'DB_API_RESTful_ProyectFinal', N'ON'
GO
ALTER DATABASE [DB_API_RESTful_ProyectFinal] SET QUERY_STORE = OFF
GO
USE [DB_API_RESTful_ProyectFinal]
GO
/****** Object:  Table [dbo].[device_manager]    Script Date: 22/04/2022 04:18:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cancer]
(
	[id] [numeric](18,0) IDENTITY (1,1) NOT NULL,
	[var1] [int]  NOT NULL,
	[var2] [int] NOT NULL,
	[var3] [int] NOT NULL,
	[var4] [int] NOT NULL,
	[var5] [int] NOT NULL,
	[var6] [int] NOT NULL,
	[var7] [int] NOT NULL,
	[var8] [int] NOT NULL,
	[var9] [int] NOT NULL,
	[resp] [int] NOT NULL
);

CREATE TABLE [dbo].[Wine]
(
	[id] [numeric](18,0) IDENTITY (1,1) NOT NULL,
	[var1] [int] NOT NULL,
	[var2] [int] NOT NULL,
	[var3] [int] NOT NULL,
	[var4] [int] NOT NULL,
	[var5] [int] NOT NULL,
	[var6] [int] NOT NULL,
	[var7] [int] NOT NULL,
	[var8] [int] NOT NULL,
	[var9] [int] NOT NULL,
	[var10] [int] NOT NULL,
	[var11] [int] NOT NULL,
	[var12] [int] NOT NULL,
	[var13] [int] NOT NULL,
	[resp] [int] NOT NULL
);

CREATE TABLE [dbo].[Iris]
(
	[id] [numeric](18,0) IDENTITY (1,1) NOT NULL,
	[var1] [int] NOT NULL,
	[var2] [int] NOT NULL,
	[var3] [int] NOT NULL,
	[var4] [int] NOT NULL,
	[resp] nvarchar(30) NOT NULL
);


CREATE TABLE [dbo].[traininCancer]
(
	[id] [numeric](18,0) IDENTITY (1,1) NOT NULL,
	[var1] [int]  NOT NULL,
	[var2] [int] NOT NULL,
	[var3] [int] NOT NULL,
	[var4] [int] NOT NULL,
	[var5] [int] NOT NULL,
	[var6] [int] NOT NULL,
	[var7] [int] NOT NULL,
	[var8] [int] NOT NULL,
	[var9] [int] NOT NULL,
	[resp] [int] NOT NULL
);

CREATE TABLE [dbo].[traininWine]
(
	[id] [numeric](18,0) IDENTITY (1,1) NOT NULL,
	[var1] [int] NOT NULL,
	[var2] [int] NOT NULL,
	[var3] [int] NOT NULL,
	[var4] [int] NOT NULL,
	[var5] [int] NOT NULL,
	[var6] [int] NOT NULL,
	[var7] [int] NOT NULL,
	[var8] [int] NOT NULL,
	[var9] [int] NOT NULL,
	[var10] [int] NOT NULL,
	[var11] [int] NOT NULL,
	[var12] [int] NOT NULL,
	[var13] [int] NOT NULL,
	[resp] [int] NOT NULL
);

CREATE TABLE [dbo].[traininIris]
(
	[id] [numeric](18,0) IDENTITY (1,1) NOT NULL,
	[var1] [int] NOT NULL,
	[var2] [int] NOT NULL,
	[var3] [int] NOT NULL,
	[var4] [int] NOT NULL,
	[resp] nvarchar(30) NOT NULL
);


/***** STORED PRODCEDURE TABLE CANCER *******/
GO
CREATE PROCEDURE [dbo].[sp_selectAllCancer]
AS
	BEGIN
		SET NOCOUNT ON;
		SELECT var1, var2, var3, var4, var5, var6, var7, var8, var9, resp FROM [dbo].[Cancer]
END


GO
CREATE PROCEDURE [dbo].[sp_insertCancer]
	@pvar1 as int,
	@pvar2 as int,
	@pvar3 as int,
	@pvar4 as int,
	@pvar5 as int,
	@pvar6 as int,
	@pvar7 as int,
	@pvar8 as int,
	@pvar9 as int,
	@presp as int
AS
	BEGIN
		SET NOCOUNT ON
		INSERT INTO [dbo].[Cancer](var1,var2,var3,var4,var5,var6,var7,var8,var9,resp)
			VALUES(@pvar1,@pvar2,@pvar3,@pvar4,@pvar5,@pvar6,@pvar7,@pvar8,@pvar9,@presp)
			 
END


GO
CREATE PROCEDURE [dbo].[sp_selectCancer]
	@pid as numeric (18,0)

AS
	BEGIN
		SET NOCOUNT ON;

		SELECT *
		FROM [dbo].[Cancer]
		WHERE id = @pid
		
END



GO
CREATE PROCEDURE [dbo].[sp_deleteCancer]
	@pid as numeric (18,0)

AS
	BEGIN
		SET NOCOUNT ON;
		DELETE [dbo].[Cancer]
		FROM [dbo].[Cancer]
		WHERE id = @pid		
END


GO
CREATE PROCEDURE [dbo].[sp_deleteAllCancer]

AS
	BEGIN
		SET NOCOUNT ON;
		TRUNCATE TABLE [dbo].[Cancer];
END


GO
CREATE PROCEDURE [dbo].[sp_updateCancer]
	@pid as numeric (18,0),
	@pvar1 as int,
	@pvar2 as int,
	@pvar3 as int,
	@pvar4 as int,
	@pvar5 as int,
	@pvar6 as int,
	@pvar7 as int,
	@pvar8 as int,
	@pvar9 as int,
	@presp as int
AS
	BEGIN
		SET NOCOUNT ON;
		UPDATE [dbo].[Cancer]
		SET var1 = @pvar1, var2 = @pvar2, var3 = @pvar3, var4 = @pvar4, var5 = @pvar5,var6 = @pvar6, var7 = @pvar7, var8 = @pvar8, var9 = @pvar9, resp = @presp
		WHERE id = @pid
END


/***** STORED PRODCEDURE TABLE WINE *******/
GO
CREATE PROCEDURE [dbo].[sp_selectAllWine]
AS
	BEGIN
		SET NOCOUNT ON;
		SELECT var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, resp FROM [dbo].[Wine]
END


GO
CREATE PROCEDURE [dbo].[sp_insertWine]
	@pvar1 as int,
	@pvar2 as int,
	@pvar3 as int,
	@pvar4 as int,
	@pvar5 as int,
	@pvar6 as int,
	@pvar7 as int,
	@pvar8 as int,
	@pvar9 as int,
	@pvar10 as int,
	@pvar11 as int,
	@pvar12 as int,
	@pvar13 as int,
	@presp as int
AS
	BEGIN
		SET NOCOUNT ON
		INSERT INTO [dbo].[Wine](var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11, var12, var13,resp)
			VALUES(@pvar1,@pvar2,@pvar3,@pvar4,@pvar5,@pvar6,@pvar7,@pvar8,@pvar9,@pvar10,@pvar11,@pvar12,@pvar13,@presp)
			 
END


GO
CREATE PROCEDURE [dbo].[sp_selectWine]
	@pid as numeric (18,0)

AS
	BEGIN
		SET NOCOUNT ON;

		SELECT *
		FROM [dbo].[Wine]
		WHERE id = @pid
		
END



GO
CREATE PROCEDURE [dbo].[sp_deleteWine]
	@pid as numeric (18,0)

AS
	BEGIN
		SET NOCOUNT ON;
		DELETE [dbo].[Wine]
		FROM [dbo].[Wine]
		WHERE id = @pid		
END


GO
CREATE PROCEDURE [dbo].[sp_deleteAllWine]

AS
	BEGIN
		SET NOCOUNT ON;
		TRUNCATE TABLE [dbo].[Wine];
END

GO
CREATE PROCEDURE [dbo].[sp_updateWine]
	@pid as numeric (18,0),
	@pvar1 as int,
	@pvar2 as int,
	@pvar3 as int,
	@pvar4 as int,
	@pvar5 as int,
	@pvar6 as int,
	@pvar7 as int,
	@pvar8 as int,
	@pvar9 as int,
	@pvar10 as int,
	@pvar11 as int,
	@pvar12 as int,
	@pvar13 as int,
	@presp as int
AS
	BEGIN
		SET NOCOUNT ON;
		UPDATE [dbo].[Wine]
		SET var1 = @pvar1, var2 = @pvar2, var3 = @pvar3, var4 = @pvar4, var5 = @pvar5,var6 = @pvar6, var7 = @pvar7, var8 = @pvar8, var9 = @pvar9, var10 = @pvar10, var11 = @pvar11,
		var12 = @pvar12, var13 = @pvar13,  resp = @presp
		WHERE id = @pid
END



/***** STORED PRODCEDURE TABLE IRIS *******/
GO
CREATE PROCEDURE [dbo].[sp_selectAllIris]
AS
	BEGIN
		SET NOCOUNT ON;
		SELECT var1, var2, var3, var4, resp FROM [dbo].[Iris]
END


GO
CREATE PROCEDURE [dbo].[sp_insertIris]
	@pvar1 as int,
	@pvar2 as int,
	@pvar3 as int,
	@pvar4 as int,
	@presp as nvarchar(30)
AS
	BEGIN
		SET NOCOUNT ON
		INSERT INTO [dbo].[Iris]
			VALUES(@pvar1,@pvar2,@pvar3,@pvar4,@presp)
			 
END


GO
CREATE PROCEDURE [dbo].[sp_selectIris]
	@pid as numeric (18,0)

AS
	BEGIN
		SET NOCOUNT ON;

		SELECT *
		FROM [dbo].[Iris]
		WHERE id = @pid
		
END



GO
CREATE PROCEDURE [dbo].[sp_deleteIris]
	@pid as numeric (18,0)
AS
	BEGIN
		SET NOCOUNT ON;
		DELETE [dbo].[Iris]
		FROM [dbo].[Iris]
		WHERE id = @pid		
END


GO
CREATE PROCEDURE [dbo].[sp_deleteAllIris]

AS
	BEGIN
		SET NOCOUNT ON;
		TRUNCATE TABLE [dbo].[Iris];
END

GO
CREATE PROCEDURE [dbo].[sp_updateIris]
	@pid as numeric (18,0),
	@pvar1 as int,
	@pvar2 as int,
	@pvar3 as int,
	@pvar4 as int,
	@presp as nvarchar(30)
AS
	BEGIN
		SET NOCOUNT ON;
		UPDATE [dbo].[Cancer]
		SET var1 = @pvar1, var2 = @pvar2, var3 = @pvar3, var4 = @pvar4,  resp = @presp
		WHERE id = @pid
END

GO
USE [DB_API_RESTful_ProyectFinal]

/***** STORED PRODCEDURE TABLE traininIRIS *******/

GO
CREATE PROCEDURE [dbo].[sp_selectAlltraininIris]

AS
	BEGIN
		SET NOCOUNT ON;

		SELECT var1, var2, var3, var4, resp
		FROM [dbo].[traininIris];

END


/***** STORED PRODCEDURE TABLE traininWine *******/

GO
CREATE PROCEDURE [dbo].[sp_selectAlltraininWine]

AS
	BEGIN
		SET NOCOUNT ON;

		SELECT var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, resp FROM [dbo].[traininWine];

END

/***** STORED PRODCEDURE TABLE traininCancer *******/

GO
CREATE PROCEDURE [dbo].[sp_selectAlltraininCancer]

AS
	BEGIN
		SET NOCOUNT ON;

		SELECT var1, var2, var3, var4, var5, var6, var7, var8, var9, resp  FROM [dbo].[traininCancer];
END

GO
USE [master]
GO
ALTER DATABASE [BD_API_RESTful_SE_2022_1] SET  READ_WRITE 




