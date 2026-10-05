## spaceattributiond

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.coremedia.figvirtualcapturecard.xpc"))
 		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.ind.xpc"))

 		APFSIOC_GET_CRYPTO_FILE_INFO
 		APFSIOC_GET_PURGEABLE_FILE_FLAGS
 		APFSIOC_GET_VOLUME_ROLE
+		APFSIOC_ITOD_OP
 		APFSIOC_LIST_ATTRIBUTION_TAGS
 		APFSIOC_PURGEABLE_GET_BULK_INFO
 		APFSIOC_PURGEABLE_GET_DETAILED_STATS
```
