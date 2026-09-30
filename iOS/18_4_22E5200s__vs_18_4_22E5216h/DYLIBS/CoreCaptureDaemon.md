## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-1255.30.0.0.0
-  __TEXT.__text: 0x38e50
+1255.31.0.0.0
+  __TEXT.__text: 0x39970
   __TEXT.__auth_stubs: 0xf50
-  __TEXT.__const: 0x4e8
+  __TEXT.__const: 0x4f0
   __TEXT.__gcc_except_tab: 0xcc
-  __TEXT.__oslogstring: 0x5fd4
-  __TEXT.__cstring: 0x72a3
+  __TEXT.__oslogstring: 0x6377
+  __TEXT.__cstring: 0x7638
   __TEXT.__unwind_info: 0x598
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x9f

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
   __AUTH_CONST.__auth_got: 0x7b8
-  __AUTH_CONST.__const: 0x1018
+  __AUTH_CONST.__const: 0xff8
   __AUTH_CONST.__cfstring: 0x960
   __DATA.__data: 0x1
   __DATA.__common: 0x4c

   - /usr/lib/libz.1.dylib
   Functions: 470
   Symbols:   851
-  CStrings:  1080
+  CStrings:  1098
 
CStrings:
+ "CCProfileMonitor 10 seconds since CCProfileMonitor initted, calling profileCallback(1) to check for installed profiles\n"
+ "CCProfileMonitor got com.apple.ManagedConfiguration.profileListChanged update, calling profileCallback(%d)\n"
+ "CCProfileMonitor::applyProfile fProfileLoaded is not set, not applying owner:%s, pipe:%s\n"
+ "CCProfileMonitor::profileCallback exiting states shutDownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n"
+ "CCProfileMonitor::profileCallback fKeyCount=0 fProfileLoaded:%d Removed\n"
+ "CCProfileMonitor::profileCallback fProfileLoaded is true, exiting\n"
+ "CCProfileMonitor::profileCallback failed to get fMutex, exiting \n"
+ "CCProfileMonitor::profileCallback setting removeProfile, exiting\n"
+ "CCProfileMonitor::profileCallback starting states shutDownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n"
+ "CCProfileMonitor::profileCallback:%d removePending token:%d fProfileLoaded:%d fProfileRemoveApplied:%d, setting removeProfile, exiting\n"
+ "CCProfileMonitor::setStreamEventHandler calling profileCallback(1)\n"
+ "CCProfileMonitor::setStreamEventHandler event received matching kXPCManagedPrefsName, no action from this handler\n"
+ "CCProfileMonitor::setStreamEventHandler eventType unhandled:%@"
+ "com.apple.MCX._managementStatusChangedForDomains"
- "CCProfileMonitor::profileCallback Removed\n"
- "CCProfileMonitor::profileCallback fProfileLoaded is true\n"
- "CCProfileMonitor::profileCallback fProfileLoaded:%d Removed\n"
- "CCProfileMonitor::profileCallback:%d removePending token:%d fProfileLoaded:%d fProfileRemoveApplied:%d\n"

```
