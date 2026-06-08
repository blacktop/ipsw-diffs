## Diagnostic-8343

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343`

```diff

-921.120.4.0.0
-  __TEXT.__text: 0x1ddc
-  __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_stubs: 0x480
-  __TEXT.__objc_methlist: 0xf4
-  __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x180
-  __TEXT.__oslogstring: 0x295
-  __TEXT.__cstring: 0x4c6
-  __TEXT.__objc_classname: 0x54
-  __TEXT.__objc_methname: 0x374
-  __TEXT.__objc_methtype: 0x115
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__got: 0x88
+1291.0.0.502.1
+  __TEXT.__text: 0x17f8
+  __TEXT.__auth_stubs: 0x260
+  __TEXT.__objc_stubs: 0x420
+  __TEXT.__objc_methlist: 0x25c
+  __TEXT.__const: 0x68
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__oslogstring: 0x235
+  __TEXT.__cstring: 0x473
+  __TEXT.__objc_classname: 0x8d
+  __TEXT.__objc_methname: 0x58d
+  __TEXT.__objc_methtype: 0x25b
+  __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__const: 0x28
-  __DATA_CONST.__cfstring: 0x280
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__cfstring: 0x2c0
+  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x118
-  __DATA.__objc_selrefs: 0x168
-  __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0xc0
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x80
+  __DATA.__objc_const: 0x388
+  __DATA.__objc_selrefs: 0x228
+  __DATA.__objc_ivar: 0xc
+  __DATA.__objc_data: 0xa0
+  __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  UUID: E8FAF3D0-4ABA-3773-BCA1-098042128E1C
-  Functions: 18
-  Symbols:   68
-  CStrings:  127
+  UUID: 22A52CF3-175B-36C9-B125-09E0A67F5406
+  Functions: 25
+  Symbols:   71
+  CStrings:  187
 
Symbols:
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_PearlFramesDecompressionInputs
+ _OBJC_METACLASS_$_PearlFramesDecompressionInputs
+ ___kCFBooleanTrue
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_new
+ _objc_retainAutorelease
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _AMSupportLogSetHandler
- _OBJC_CLASS_$_CRUtils
- _OBJC_CLASS_$_NSNumber
- __logHandler
- _objc_release_x27
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
CStrings:
+ "#16@0:8"
+ "%s: %@, %@"
+ "-[PearlFramesDecompressionController setupWithInputs:responder:]"
+ "-[PearlFramesDecompressionController updateDATFirmware:]"
+ "-[PearlFramesDecompressionInputs validateAndInitializeParameters:]"
+ "@\"NSString\"16@0:8"
+ "@\"PearlFramesDecompressionInputs\""
+ "@24@0:8:16"
+ "@24@0:8@16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "B"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"NSDictionary\"16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B24@0:8^@16"
+ "B32@0:8^@16^@24"
+ "BOOLFromKey:defaultValue:failed:"
+ "DKDiagnosticInputs"
+ "Get response timeout from corerepaird for DAT update"
+ "NO"
+ "NSObject"
+ "PearlFramesDecompressionInputs"
+ "Q16@0:8"
+ "Start to update Pearl firmware ..."
+ "Start to update Yonkers firmware ..."
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"PearlFramesDecompressionInputs\",&,N,V_inputs"
+ "TB,R,N,V_updateYonkersOnly"
+ "TQ,R"
+ "Update DAT firmware got response from corerepaird, error: %@"
+ "Update Pearl firmware successfully"
+ "Update Yonkers firmware successfully"
+ "Vv16@0:8"
+ "YES"
+ "^{_NSZone=}16@0:8"
+ "_inputs"
+ "_updateYonkersOnly"
+ "autorelease"
+ "class"
+ "conformsToProtocol:"
+ "debugDescription"
+ "description"
+ "hash"
+ "inputs"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "setInputs:"
+ "setupWithInputs:responder:"
+ "stringWithFormat:"
+ "superclass"
+ "updateDATFirmware:"
+ "updateDATFirmware:withReply:"
+ "updatePearl:lastSeenError:"
+ "updateSavage"
+ "updateYonkers"
+ "updateYonkers:"
+ "updateYonkersOnly"
+ "updateYonkersOnly: %@"
+ "v24@0:8@16"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@16@24"
+ "validateAndInitializeParameters:"
+ "validateAndInitializePredicates:"
+ "validateAndInitializeSpecifications:"
+ "zone"
- "-[PearlFramesDecompressionController preCheck]"
- "-[PearlFramesDecompressionController updateBrunorDATFirmware]"
- "-[PearlFramesDecompressionController updateSavageDATFirmware]"
- "Failed to mount hardware partition"
- "Get response timeout from corerepaird for Brunor update"
- "Get response timeout from corerepaird for Savage update"
- "PearlFramesDecompressionLastSeenErrorCode"
- "PearlFramesDecompressionLastSeenErrorDescription"
- "Start to update Brunor/Yonkers firmware ..."
- "Start to update Savage/Yonkers firmware ..."
- "Update Brunor firmware got response from corerepaird, error: %@"
- "Update Brunor/Yonkers firmware successfully"
- "Update Savage firmware got response from corerepaird, error: %@"
- "Update Savage/Yonkers firmware successfully"
- "code"
- "getInnermostNSError:"
- "localizedDescription"
- "numberWithInteger:"
- "preCheck"
- "updateBrunorDATFirmware"
- "updateBrunorDATFirmwareWithReply:"
- "updateSavageDATFirmware"
- "updateSavageDATFirmwareWithReply:"

```
