from sylk.commons.protos.sylk.SylkConfigs.v1.SylkConfigs_pb2 import SylkCliConfigs
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
    token="sylk_97143301-7fba-44a0-8779-b8ceeb3c3183",
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

sylk_api_host='localhost'
sylk_api_port=9000