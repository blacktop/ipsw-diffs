## proximitycontrold

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationmanager"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
+		(require-not (global-name "com.apple.assistant.dictation"))
 		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
