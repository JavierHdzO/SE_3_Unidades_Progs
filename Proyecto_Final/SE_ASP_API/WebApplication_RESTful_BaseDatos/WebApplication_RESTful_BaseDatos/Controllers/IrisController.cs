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
    public class IrisController : ApiController
    {
        // GET: api/cancer
        public DataTable Get()
        {
            Handler_DatabaseIris handler = new Handler_DatabaseIris();
            return handler.SelectALL_TestIris();
        }

        // GET: cancer/Details/5
        public DataTable Get(int id)
        {
            Handler_DatabaseIris handler = new Handler_DatabaseIris();
            return handler.SelectALL_TraininIris();
        }

        // POST api/cancer
        public int Post([FromBody] Handler_DatabaseIris handler)
        {
            int v = handler.Insert_Test(); //Consider SET NOCOUNT ON / OFF
            return v;

        }

        public int Delete()
        {
            Handler_DatabaseIris handler = new Handler_DatabaseIris();
            int v = handler.Delete_AllTest();
            return v;
        }
    }
}
