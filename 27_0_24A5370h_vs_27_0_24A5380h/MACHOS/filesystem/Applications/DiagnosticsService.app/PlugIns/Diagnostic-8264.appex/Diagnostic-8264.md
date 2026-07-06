## Diagnostic-8264

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264`

```diff

-  __TEXT.__text: 0x4888
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_stubs: 0xe80
-  __TEXT.__objc_methlist: 0x35c
-  __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__cstring: 0x820
-  __TEXT.__oslogstring: 0x79c
+  __TEXT.__text: 0x4c18
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0xfc0
+  __TEXT.__objc_methlist: 0x38c
+  __TEXT.__const: 0xa0
+  __TEXT.__gcc_except_tab: 0x1a8
+  __TEXT.__cstring: 0x877
+  __TEXT.__oslogstring: 0x896
   __TEXT.__objc_classname: 0x92
-  __TEXT.__objc_methname: 0xded
-  __TEXT.__objc_methtype: 0x2c4
+  __TEXT.__objc_methname: 0xf0d
+  __TEXT.__objc_methtype: 0x32a
   __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__const: 0x78
-  __DATA_CONST.__cfstring: 0x880
+  __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x1f0
-  __DATA_CONST.__got: 0x160
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x620
-  __DATA.__objc_selrefs: 0x4b0
-  __DATA.__objc_ivar: 0x38
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x130
+  __DATA.__objc_const: 0x680
+  __DATA.__objc_selrefs: 0x500
+  __DATA.__objc_ivar: 0x40
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 60
-  Symbols:   121
-  CStrings:  429
+  Functions: 68
+  Symbols:   111
+  CStrings:  462
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _CFRelease
+ _OBJC_CLASS_$_CRBatteryUpdaterFactory
- _CFStringGetCStringPtr
- _T200GetBoardIdFromDT
- _T200UpdaterCreate
- _T200UpdaterExecCommand
- _T200UpdaterIsDone
- _kT200OptionRestoreInternal
- _kT200OptionUpdateType
- _kT200PreflightContextLimited
- _kT200SkipFirmwareMapStore
- _kT200TagDeferredCommit
- _kT200TagFWSkipSameVersion
- _kT200TagPreflightContext
CStrings:
+ "%@,Ticket"
+ "@\"<CRBatteryUpdaterProtocol>\""
+ "Battery firmware updater setup successful"
+ "DeferredCommit"
+ "FWSkipSameVersion"
+ "Failed to setup firmware updater with options during retry, error:%@"
+ "Failed to setup firmware updater with options, error:%@"
+ "Limited"
+ "No need to update battery FW"
+ "PreflightContext"
+ "RestoreInternal"
+ "SkipFirmwareMapStore"
+ "T@\"<CRBatteryUpdaterProtocol>\",&,N,V_updater"
+ "T^{__CFDictionary=},N,V_updaterOptions"
+ "UpdateType"
+ "^{__CFDictionary=}"
+ "^{__CFDictionary=}16@0:8"
+ "_updater"
+ "_updaterOptions"
+ "execCommand(kFWUpdaterCmdQueryInfo) returns successfully, but deviceInfoDict is nil"
+ "execCommand:input:output:error:"
+ "getBMUTicketForBatteryFWUpdateWithOptions:BMUTicket:error:"
+ "getBMUType"
+ "getBoardIdFromDT:error:"
+ "isDone:"
+ "self.updaterOptions failed to allocate"
+ "setUpdater:"
+ "setUpdaterOptions:"
+ "setupWithOptions:logFunction:error:"
+ "sharedInstance"
+ "updater"
+ "updater execCommand failed to query battery information:%@"
+ "updater failed to perform next stage: %@:%@"
+ "updater isDone failed:%@"
+ "updaterOptions"
+ "v24@0:8^{__CFDictionary=}16"
- "Created the Veridian Updater"
- "Failed to create %s obj::error:%@"
- "No need to update Veridian FW"
- "T200"
- "T200UpdaterExecCommand failed: %@:%@"
- "T200UpdaterExecCommand failed:%@"
- "Veridian symbols absent"
- "getBMUTicketForVeridianFWUpdateWithOptions:BMUTicket:error:"
- "updaterOptions failed to allocate"

```
