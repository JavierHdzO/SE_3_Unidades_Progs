using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Web;

namespace WebApplication_RESTful_BaseDatos.Models
{
    public class Handler_DatabaseCancer
    {
        #region Propierties (Variables)
        public int Id { get; set; }
        public int Var1 { get; set; }
        public int Var2 { get; set; }
        public int Var3 { get; set; }
        public int Var4 { get; set; }
        public int Var5 { get; set; }
        public int Var6 { get; set; }
        public int Var7 { get; set; }
        public int Var8 { get; set; }
        public int Var9 { get; set; }
        public int Resp { get; set; }

        public override string ToString()
        {
            return "Id "+Id+" Var1 "+Var1+ " Var2 "+Var2+" Var3 "+Var3+" Var4 "+Var4+" Var5 "+Var5+ " Var6 "+Var6+" Var7 "+Var7+" Var8 "+Var8+" Var9 "+Var9+" Resp "+Resp;
        }
        #endregion

        #region Contructors
        // Use for SelectAll
        public Handler_DatabaseCancer() { }

        // Use for Insert
        public Handler_DatabaseCancer(int var1, int var2, int var3, int var4, int var5, int var6, int var7, int var8, int var9, int resp) 
        {
            Var1 = var1;
            Var2 = var2;
            Var3 = var3;
            Var4 = var4;
            Var5 = var5;
            Var6 = var6;
            Var7 = var7;
            Var8 = var8;
            Var9 = var9;
            Resp = resp;
        }

        // Use for update


        public Handler_DatabaseCancer(int id, int var1, int var2, int var3, int var4, int var5, int var6, int var7, int var8, int var9, int resp) 
        {
            Id = id;
            Var1 = var1;
            Var2 = var2;
            Var3 = var3;
            Var4 = var4;
            Var5 = var5;
            Var6 = var6;
            Var7 = var7;
            Var8 = var8;
            Var9 = var9;
            Resp = resp;

        }



        //Use for Select and Delete
        public Handler_DatabaseCancer(int id)
        {
            Id = id;
        }
        #endregion

        #region CRUD_Cancer

        public DataTable SelectALL_TraininCancer()
        {
            SqlConnection con = new SqlConnection(ConfigurationManager.ConnectionStrings["connectionDB"].ToString());
            con.Open();


            //sp_selectAlltraininCancer
            SqlCommand cmd = new SqlCommand("sp_selectAlltraininCancer", con);
            cmd.CommandType = System.Data.CommandType.StoredProcedure;

            //EXEC SP
            SqlDataAdapter da = new SqlDataAdapter(cmd);

            DataTable dt = new DataTable("traininCancer_Info");//recommended
            da.Fill(dt);

            con.Close();

            return dt;

        }

        public DataTable SelectALL_TestCancer()
        {
            SqlConnection con = new SqlConnection(ConfigurationManager.ConnectionStrings["connectionDB"].ToString());
            con.Open();


            //sp_selectCancer
            SqlCommand cmd = new SqlCommand("sp_selectAllCancer", con);
            cmd.CommandType = System.Data.CommandType.StoredProcedure;

            //EXEC SP
            SqlDataAdapter da = new SqlDataAdapter(cmd);

            DataTable dt = new DataTable("testCancer_Info");//recommended
            da.Fill(dt);

            con.Close();

            return dt;

        }




        public int Insert_Test()
        {
            SqlConnection con = new SqlConnection(ConfigurationManager.ConnectionStrings["connectionDB"].ToString());
            con.Open();

            SqlCommand cmd = new SqlCommand("sp_insertCancer", con);
            cmd.CommandType = System.Data.CommandType.StoredProcedure;

            //PARAMETER 1 
            SqlParameter Param_var1= new SqlParameter();
            Param_var1.ParameterName = "@pvar1";
            Param_var1.Value = Var1;
            Param_var1.Direction = System.Data.ParameterDirection.Input;
            cmd.Parameters.Add(Param_var1);


            //PARAMETER 2
            SqlParameter Param_var2 = new SqlParameter();
            Param_var2.ParameterName = "@pvar2";
            Param_var2.Value = Var2;
            Param_var2.Direction = System.Data.ParameterDirection.Input;
            cmd.Parameters.Add(Param_var2);

            //PARAMETER 3 
            SqlParameter Param_var3 = new SqlParameter();
            Param_var3.ParameterName = "@pvar3";
            Param_var3.Value = Var3;
            Param_var3.Direction = System.Data.ParameterDirection.Input;
            cmd.Parameters.Add(Param_var3);

            //PARAMETER 4
            SqlParameter Param_var4 = new SqlParameter();
            Param_var4.ParameterName = "@pvar4";
            Param_var4.Value = Var4;
            Param_var4.Direction = System.Data.ParameterDirection.Input;
            cmd.Parameters.Add(Param_var4);

            //PARAMETER 5
            SqlParameter Param_var5 = new SqlParameter();
            Param_var5.ParameterName = "@pvar5";
            Param_var5.Value = Var5;
            Param_var5.Direction = System.Data.ParameterDirection.Input;
            cmd.Parameters.Add(Param_var5);

            //PARAMETER 6
            SqlParameter Param_var6 = new SqlParameter();
            Param_var6.ParameterName = "@pvar6";
            Param_var6.Value = Var6;
            Param_var6.Direction = System.Data.ParameterDirection.Input;
            cmd.Parameters.Add(Param_var6);

            //PARAMETER 7
            SqlParameter Param_var7 = new SqlParameter();
            Param_var7.ParameterName = "@pvar7";
            Param_var7.Value = Var7;
            Param_var7.Direction = System.Data.ParameterDirection.Input;
            cmd.Parameters.Add(Param_var7);

            //PARAMETER 8
            SqlParameter Param_var8 = new SqlParameter();
            Param_var8.ParameterName = "@pvar8";
            Param_var8.Value = Var8;
            Param_var8.Direction = System.Data.ParameterDirection.Input;
            cmd.Parameters.Add(Param_var8);

            //PARAMETER 9
            SqlParameter Param_var9 = new SqlParameter();
            Param_var9.ParameterName = "@pvar9";
            Param_var9.Value = Var9;
            Param_var9.Direction = System.Data.ParameterDirection.Input;
            cmd.Parameters.Add(Param_var9);

            //PARAMETER 10
            SqlParameter Param_resp = new SqlParameter();
            Param_resp.ParameterName = "@presp";
            Param_resp.Value = Resp;
            Param_resp.Direction = System.Data.ParameterDirection.Input;
            cmd.Parameters.Add(Param_resp);

            //EXEC SP
            int v = cmd.ExecuteNonQuery();

            con.Close();

            return v;
        }

        public int Delete_AllTest()
        {
            SqlConnection con = new SqlConnection(ConfigurationManager.ConnectionStrings["connectionDB"].ToString());
            con.Open();

            SqlCommand cmd = new SqlCommand("sp_deleteAllCancer", con); //really? 
            cmd.CommandType = System.Data.CommandType.StoredProcedure;
            //EXEC SP
            int v = cmd.ExecuteNonQuery();

            con.Close();

            return v;

        }

        #endregion

    }
}