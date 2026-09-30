## ManifestStorageService

> Group: ⬆️ Updated

```diff

 (deny sysctl-write
 	(require-all
 		(sysctl-name "vm.debug_range_enabled")
-		(require-not (sysctl-name "security.mac.image4.nonce.copy_hash"))
 		(require-not (sysctl-name "security.mac.image4.image.dfu"))
 		(require-not (sysctl-name "vm.debug_range_enabled"))
+		(require-not (sysctl-name "security.mac.image4.nonce.copy_hash"))
 		(require-not (sysctl-name "kern.wq_limit_cooperative_threads"))
 		(require-not (system-attribute developer-mode))
 	)
```
