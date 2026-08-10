## FileBrowsingPathResolver

> Group: ⬆️ Updated

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "AppleAPFSUserClient")
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 	)
 )
 

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.bird.token"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.coresymbolicationd"))
 		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (global-name "com.apple.cache_delete"))
+		(require-not (global-name "com.apple.dmd.policy"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
