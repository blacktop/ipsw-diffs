## profiled

> `/usr/libexec/profiled`

```diff

-2425.0.0.0.0
-  __TEXT.__text: 0xa0574
-  __TEXT.__auth_stubs: 0x20d0
-  __TEXT.__objc_stubs: 0x105c0
-  __TEXT.__objc_methlist: 0x5ad4
+2426.1.0.0.0
+  __TEXT.__text: 0xa0550
+  __TEXT.__auth_stubs: 0x20e0
+  __TEXT.__objc_stubs: 0x10560
+  __TEXT.__objc_methlist: 0x5acc
   __TEXT.__const: 0x20e
-  __TEXT.__gcc_except_tab: 0x1c2c
-  __TEXT.__oslogstring: 0xd7de
-  __TEXT.__cstring: 0x8a1e
-  __TEXT.__objc_methname: 0x145bf
+  __TEXT.__gcc_except_tab: 0x1c24
+  __TEXT.__oslogstring: 0xd761
+  __TEXT.__cstring: 0x89ff
+  __TEXT.__objc_methname: 0x14566
   __TEXT.__objc_classname: 0xb5b
-  __TEXT.__objc_methtype: 0x224d
+  __TEXT.__objc_methtype: 0x2239
   __TEXT.__unwind_info: 0x1748
-  __DATA_CONST.__auth_got: 0x1078
-  __DATA_CONST.__got: 0x1bc0
+  __DATA_CONST.__auth_got: 0x1080
+  __DATA_CONST.__got: 0x1bb8
   __DATA_CONST.__const: 0x1b90
-  __DATA_CONST.__cfstring: 0x85c0
+  __DATA_CONST.__cfstring: 0x85e0
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x6588
-  __DATA.__objc_selrefs: 0x48f8
+  __DATA.__objc_selrefs: 0x48e0
   __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x540

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 503EF65C-AC18-33E0-8DA0-5FF59D1480E3
-  Functions: 2046
+  UUID: 185FD153-3A9A-30CE-BC07-911DC0917985
+  Functions: 2045
   Symbols:   1459
-  CStrings:  6142
+  CStrings:  6136
 
Symbols:
+ _MCKeybagVerifyPasscodeContext
+ _kMDMSettingsURLDownloadedProfile
+ _kMDMSettingsURLResourceID
- _OBJC_CLASS_$_MOEffectiveSettingsStore
- _kMCSettingsURLProfilePurgatoryInstallation
- _kMDMLAPasscodeContextKey
CStrings:
+ "%@?%@=%@"
+ "-[MCInteractionClient requestCurrentPasscodeOutPasscodeContext:]"
+ "B28@0:8B16^@20"
+ "MCMigrator: Updating isADEProfile value..."
+ "_requestCurrentPasscodeExtractable:outPasscodeContext:"
+ "isADEProfile"
+ "requestCurrentPasscodeOutPasscodeContext:"
- "-[MCInteractionClient requestCurrentPasscodeOutPasscodeContext:isLAContext:]"
- "B32@0:8^@16^B24"
- "B36@0:8B16^@20^B28"
- "Have passcodeContext from ACMContext"
- "Have passcodeContext from LAContext"
- "ScreenTime"
- "Unable to create extractable passcode context wrapper from passcode context. Error: %{public}@"
- "_requestCurrentPasscodeExtractable:outPasscodeContext:isLAContext:"
- "blockedByFilter"
- "didEnrollInMDMWithPasscode:duringMigration:"
- "policy"
- "requestCurrentPasscodeOutPasscodeContext:isLAContext:"
- "simplified_agent"
- "webContent"

```
