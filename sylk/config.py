from sylk.commons.protos.SylkConfigs_pb2 import SylkCliConfigs
"""
               ____  
   _______  __/ / /__
  / ___/ / / / / //_/
 (__  ) /_/ / / ,<   
/____/\__, /_/_/|_|  
     /____/ 
     
sylk cli module configuration"""
configs=SylkCliConfigs(
    host="localhost",
    port=44880,
    # Analytic gathering approval
    analytics=False,
    # First run flag
    first_run=False,
    token="sylk_2d248296-5a4a-467f-b50d-0436aeec1b5a",
    # Supported builtins templates
    sylk_templates = [
        "@sylk/Blank",
        "@sylk/TodoAppPy"
        # "@sylk/io",
        # "@sylk/SamplePy",
        # "@sylk/SampleTs",
        # "@sylk/PubSubTs",
        # "@sylk/HelloWorldPy",
        # "@sylk/HelloWorldTs"
    ]
)
