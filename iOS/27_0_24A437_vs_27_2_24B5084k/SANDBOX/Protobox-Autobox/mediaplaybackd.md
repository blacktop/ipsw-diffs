## mediaplaybackd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.BTAudioHALPlugin.xpc"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.wifi.manager"))
 		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
