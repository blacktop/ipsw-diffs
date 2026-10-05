## healthd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
 		(require-not (global-name "com.apple.siri.external_request"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (global-name "com.apple.diagnosticpipeline.service"))
 		(require-not (global-name "com.apple.triald.namespace-management"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled"))
```
