using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using WebApplication_RESTful_BaseDatos.Models;

namespace WebApplication_RESTful_BaseDatos.Controllers
{
    public class cancerController : ApiController
    {
        // GET: api/cancer2
        // GET: cancer
        public DataTable Get()
        {
            Handler_DatabaseCancer handler = new Handler_DatabaseCancer();
            return handler.SelectALL_TestCancer();
        }

        // GET: cancer/Details/5
        public DataTable Get(int id)
        {
            Handler_DatabaseCancer handler = new Handler_DatabaseCancer();
            return handler.SelectALL_TraininCancer();
        }

        // POST api/cancer
        public int Post([FromBody] Handler_DatabaseCancer handler)
        {
            int v = handler.Insert_Test(); //Consider SET NOCOUNT ON / OFF
            return v;
        }


        public int Delete() 
        {
            Handler_DatabaseCancer handler = new Handler_DatabaseCancer();
            int v = handler.Delete_AllTest();
            return v;
        }




    }
}
