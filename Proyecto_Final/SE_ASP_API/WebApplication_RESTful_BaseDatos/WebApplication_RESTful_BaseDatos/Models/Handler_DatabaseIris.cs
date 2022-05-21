using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Web;

namespace WebApplication_RESTful_BaseDatos.Models
{
    public class Handler_DatabaseIris
    {

        #region Propierties (Variables)
        public int Id { get; set; }
        public int Var1 { get; set; }
        public int Var2 { get; set; }
        public int Var3 { get; set; }
        public int Var4 { get; set; }

        public string Resp{ get; set; }


        public override string ToString()
        {
            return "Id " + Id + " Var1 " + Var1 + " Var2 " + Var2 + " Var3 " + Var3 + " Var4 " + Var4 + " Resp " + Resp;
        }

        #endregion

        #region Contructors
        // Use for SelectAll
        public Handler_DatabaseIris() { }

        // Use for Insert
        public Handler_DatabaseIris(int var1, int var2, int var3, int var4, string resp)
        {
            Var1 = var1;
            Var2 = var2;
            Var3 = var3;
            Var4 = var4;
            Resp = resp;
        }

        // Use for update

        public Handler_DatabaseIris(int id, int var1, int var2, int var3, int var4, string resp)
        {
            Id = id;
            Var1 = var1;
            Var2 = var2;
            Var3 = var3;
            Var4 = var4;
            Resp = resp;

        }



        //Use for Select and Delete
        public Handler_DatabaseIris(int id)
        {
            Id = id;
        }
        #endregion

        #region CRUD_Iris

        public DataTable SelectALL_TraininIris()
        {
            SqlConnection con = new SqlConnection(ConfigurationManager.ConnectionStrings["connectionDB"].ToString());
            con.Open();


            //sp_selectAlltraininCancer
            SqlCommand cmd = new SqlCommand("sp_selectAlltraininIris", con);
            cmd.CommandType = System.Data.CommandType.StoredProcedure;

            //EXEC SP
            SqlDataAdapter da = new SqlDataAdapter(cmd);

            DataTable dt = new DataTable("traininCancer_Info");//recommended
            da.Fill(dt);

            con.Close();

            return dt;

        }

        public DataTable SelectALL_TestIris()
        {
            SqlConnection con = new SqlConnection(ConfigurationManager.ConnectionStrings["connectionDB"].ToString());
            con.Open();


            //sp_selectCancer
            SqlCommand cmd = new SqlCommand("sp_selectAllIris", con);
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

            SqlCommand cmd = new SqlCommand("sp_insertIris", con);
            cmd.CommandType = System.Data.CommandType.StoredProcedure;

            //PARAMETER 1 
            SqlParameter Param_var1 = new SqlParameter();
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

            SqlCommand cmd = new SqlCommand("sp_deleteAllIris", con); //really? 
            cmd.CommandType = System.Data.CommandType.StoredProcedure;
            //EXEC SP
            int v = cmd.ExecuteNonQuery();

            con.Close();

            return v;

        }

        #endregion
    }
}