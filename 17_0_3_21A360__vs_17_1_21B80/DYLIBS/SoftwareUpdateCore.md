## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-1856.2.2.0.0
-  __TEXT.__text: 0xf5218
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x65f0
-  __TEXT.__cstring: 0x11605
-  __TEXT.__oslogstring: 0xa7c2
+1856.42.1.0.0
+  __TEXT.__text: 0xf5954
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_methlist: 0x6648
+  __TEXT.__cstring: 0x11732
+  __TEXT.__oslogstring: 0xa819
   __TEXT.__gcc_except_tab: 0x68c
-  __TEXT.__const: 0x40
+  __TEXT.__const: 0x48
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x18d4
-  __TEXT.__objc_classname: 0x655
-  __TEXT.__objc_methname: 0x11d70
+  __TEXT.__unwind_info: 0x18e8
+  __TEXT.__objc_classname: 0x657
+  __TEXT.__objc_methname: 0x11e92
   __TEXT.__objc_methtype: 0xd8b
-  __TEXT.__objc_stubs: 0xca80
+  __TEXT.__objc_stubs: 0xcb40
   __DATA_CONST.__got: 0x438
   __DATA_CONST.__const: 0x1c00
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7a58
-  __DATA_CONST.__objc_selrefs: 0x39a0
+  __DATA_CONST.__objc_const: 0x7ae8
+  __DATA_CONST.__objc_selrefs: 0x39e8
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__cfstring: 0x10180
+  __AUTH_CONST.__cfstring: 0x101c0
   __AUTH_CONST.__objc_const: 0x1df8
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__auth_got: 0x348
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_classrefs: 0x388
+  __DATA.__objc_classrefs: 0x390
   __DATA.__objc_superrefs: 0x1a8
-  __DATA.__objc_ivar: 0x820
+  __DATA.__objc_ivar: 0x82c
   __DATA.__data: 0x300
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0xb90

   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
+  - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1B16017-BDD9-3C18-8B68-0F7F76A895A6
-  Functions: 2545
-  Symbols:   8639
-  CStrings:  7643
+  UUID: 04DE48E6-2543-388A-9C96-3D1CFF43BD78
+  Functions: 2552
+  Symbols:   8666
+  CStrings:  7671
 
Symbols:
+ -[SUCoreDDMActivityScheduler pcTimer]
+ -[SUCoreDDMActivityScheduler setPcTimer:]
+ -[SUCoreDDMActivityScheduler setUsePCSimpleTimer:]
+ -[SUCoreDDMActivityScheduler setUseXPC:]
+ -[SUCoreDDMActivityScheduler usePCSimpleTimer]
+ -[SUCoreDDMActivityScheduler useXPC]
+ -[SUCoreDescriptor refreshInstallationSize]
+ _OBJC_CLASS_$_PCSimpleTimer
+ _OBJC_IVAR_$_SUCoreDDMActivityScheduler._pcTimer
+ _OBJC_IVAR_$_SUCoreDDMActivityScheduler._usePCSimpleTimer
+ _OBJC_IVAR_$_SUCoreDDMActivityScheduler._useXPC
+ __unnamed_array_storage.676
+ __unnamed_array_storage.688
+ __unnamed_array_storage.709
+ _objc_msgSend$initWithFireDate:serviceIdentifier:target:selector:userInfo:
+ _objc_msgSend$pcTimer
+ _objc_msgSend$scheduleInRunLoop:
+ _objc_msgSend$setPcTimer:
+ _objc_msgSend$usePCSimpleTimer
+ _objc_msgSend$useXPC
+ _time
+ _xpc_dictionary_set_date
+ _xpc_set_event
- __unnamed_array_storage.673
- __unnamed_array_storage.685
- __unnamed_array_storage.706
CStrings:
+ "\x15"
+ "-[SUCoreDDMActivityScheduler armActivitySchedulerWithDate:options:]"
+ "Date"
+ "Internal error: failed to get the shared device"
+ "Invalid declaration: invalid enforced install date"
+ "Invalid declaration: no target version set"
+ "T@\"NSString\",R,&"
+ "T@\"SUCoreDocumentation\",&,V_documentation"
+ "T@,&,V_pcTimer"
+ "TB,N,V_usePCSimpleTimer"
+ "TB,N,V_useXPC"
+ "[DDM] %s: Using NSTimer"
+ "[DDM] %s: Using PCSimpleTimer"
+ "[DDM] %s: Using XPC alarm stream"
+ "_pcTimer"
+ "_usePCSimpleTimer"
+ "_useXPC"
+ "com.apple.MobileSoftwareUpdate.DDMActivityScheduler"
+ "com.apple.SoftwareUpdateCore.DDMActivityScheduler"
+ "com.apple.alarm"
+ "initWithFireDate:serviceIdentifier:target:selector:userInfo:"
+ "pcTimer"
+ "refreshInstallationSize"
+ "scheduleInRunLoop:"
+ "setPcTimer:"
+ "setUsePCSimpleTimer:"
+ "setUseXPC:"
+ "unable to determine refreshed apply size for installation, using preexisting value"
+ "usePCSimpleTimer"
+ "useXPC"
- "Failed to get the shared device"
- "Invalid declaration: nil enforced install date"
- "Invalid declaration: no version set"
- "T@\"SUCoreDocumentation\",&,N,V_documentation"

```
