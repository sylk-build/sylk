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
    token=None,
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
