## searchtoold

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.imagent.embedded.auth"))
 		(require-not (global-name "com.apple.medialibraryd.xpc"))
+		(require-not (global-name "com.apple.generativeexperiences.generativeexperiencessession"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Contact"))
 		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
 		(require-not (global-name "com.apple.gpumemd.source"))

 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner"))
 		(require-not (xpc-service-name "com.apple.imdpersistence.IMDPersistenceAgent"))
+		(require-not (xpc-service-name "com.apple.StocksKitService"))
 		(require-not (xpc-service-name "com.apple.FileBrowsingServices.PathResolver"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.FSEvents"))
```
