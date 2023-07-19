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
    token="sylk_967c2e81-1b96-441c-b9a0-cff33c38cb79",
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