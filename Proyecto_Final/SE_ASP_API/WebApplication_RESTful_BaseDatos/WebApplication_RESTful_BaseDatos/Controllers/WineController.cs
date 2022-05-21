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
    public class WineController : ApiController
    {
        // GET: api/cancer2
        // GET: cancer
        public DataTable Get()
        {
            Handler_DatabaseWine handler = new Handler_DatabaseWine();
            return handler.SelectALL_TestWine();
        }

        // GET: cancer/Details/5
        public DataTable Get(int id)
        {
            Handler_DatabaseWine handler = new Handler_DatabaseWine();
            return handler.SelectALL_TraininWine();
        }

        // POST api/cancer
        public int Post([FromBody] Handler_DatabaseWine handler)
        {
            int v = handler.Insert_Test(); //Consider SET NOCOUNT ON / OFF
            return v;

        }


        public int Delete()
        {
            Handler_DatabaseWine handler = new Handler_DatabaseWine();
            int v = handler.Delete_AllTest();
            return v;
        }
    }
}
