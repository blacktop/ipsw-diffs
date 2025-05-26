## ptpcamerad

> `/usr/libexec/ptpcamerad`

```diff

-1873.2.4.0.0
-  __TEXT.__text: 0x28654
+1873.3.2.0.0
+  __TEXT.__text: 0x28b04
   __TEXT.__auth_stubs: 0xa50
-  __TEXT.__objc_stubs: 0x4180
-  __TEXT.__objc_methlist: 0x2a34
-  __TEXT.__objc_methname: 0x6238
-  __TEXT.__cstring: 0x6e2d
+  __TEXT.__objc_stubs: 0x4200
+  __TEXT.__objc_methlist: 0x2a9c
+  __TEXT.__objc_methname: 0x641e
+  __TEXT.__cstring: 0x6ec7
   __TEXT.__objc_classname: 0x34d
-  __TEXT.__objc_methtype: 0xcea
+  __TEXT.__objc_methtype: 0xd06
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x39c
   __TEXT.__oslogstring: 0x3f
   __TEXT.__ustring: 0xb8
-  __TEXT.__unwind_info: 0x864
+  __TEXT.__unwind_info: 0x868
   __DATA_CONST.__auth_got: 0x538
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0x8c8
-  __DATA_CONST.__cfstring: 0x7580
+  __DATA_CONST.__cfstring: 0x7640
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_arraydata: 0x28b0
   __DATA_CONST.__objc_dictobj: 0x21c0
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x4ab8
-  __DATA.__objc_selrefs: 0x19a8
+  __DATA.__objc_const: 0x4b58
+  __DATA.__objc_selrefs: 0x19f0
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x1e8
   __DATA.__objc_superrefs: 0x118
-  __DATA.__objc_ivar: 0x474
+  __DATA.__objc_ivar: 0x480
   __DATA.__objc_data: 0xaf0
   __DATA.__data: 0x2a8
   __DATA.__bss: 0x58

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1040
+  Functions: 1049
   Symbols:   253
-  CStrings:  2435
+  CStrings:  2457
 
CStrings:
+ "%@: 0x%08X"
+ "0x%08X:%lu"
+ "> Existing Device | locID - 0x%08llX"
+ "> New Device | locID - 0x%08llX"
+ "@\"OS_remote_device_browser\""
+ "Already Browsing: 0x%08X"
+ "Canceled: 0x%08X"
+ "Ignored: 0x%08llX"
+ "Invalid Device: 0x%08X"
+ "Monitoring"
+ "PTP-Enumeration-Timer-Queue:0x%08X"
+ "PTP-MobdevProperties-Queue:0x%08X"
+ "Received: %llu on 0x%08X"
+ "RemoteServices"
+ "T@\"NSMutableDictionary\",&,V_mobdevProperties"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_mobdevPropertiesQueue"
+ "T@\"OS_remote_device_browser\",&,N,V_mobdevPropertiesBrowser"
+ "T{os_unfair_lock_s=I},N,V_mobdevPropertiesLock"
+ "Updated: 0x%08X"
+ "_USBPTPInterfaceDeath | locID - 0x%08llX"
+ "_mobdevPropertiesBrowser"
+ "_mobdevPropertiesLock"
+ "_mobdevPropertiesQueue"
+ "abortPipe locID"
+ "addMobdevProperties:"
+ "mobdevProperties"
+ "mobdevPropertiesBrowser"
+ "mobdevPropertiesLock"
+ "mobdevPropertiesQueue"
+ "setMobdevProperties:"
+ "setMobdevPropertiesBrowser:"
+ "setMobdevPropertiesLock:"
+ "setMobdevPropertiesQueue:"
- "%@:%lu"
- "*** abortPendingIO"
- "> Existing Device"
- "> New Device: %lu"
- "PTP-Notify-Enumerating"
- "Received: %llu on 0x%x"
- "Updated: %d"
- "_USBPTPInterfaceDeath: %lu"
- "begin monitoring remote services"
- "remote services"
- "rs-browser-queue"

```
