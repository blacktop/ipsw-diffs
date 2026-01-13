## fdesetup

> `/usr/bin/fdesetup`

```diff

-1798.80.2.0.0
-  __TEXT.__text: 0x2e3dc
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_stubs: 0x26c0
+1798.80.3.0.0
+  __TEXT.__text: 0x2f0c8
+  __TEXT.__auth_stubs: 0xfb0
+  __TEXT.__objc_stubs: 0x2780
   __TEXT.__objc_methlist: 0x61c
-  __TEXT.__const: 0xf9
+  __TEXT.__const: 0x109
   __TEXT.__gcc_except_tab: 0x9b0
-  __TEXT.__oslogstring: 0x9621
-  __TEXT.__cstring: 0xf402
+  __TEXT.__oslogstring: 0x98bf
+  __TEXT.__cstring: 0xf723
   __TEXT.__objc_classname: 0x6d
-  __TEXT.__objc_methname: 0x2341
+  __TEXT.__objc_methname: 0x23c5
   __TEXT.__objc_methtype: 0x377
   __TEXT.__unwind_info: 0x740
-  __DATA_CONST.__auth_got: 0x7e0
-  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__auth_got: 0x7e8
+  __DATA_CONST.__got: 0x390
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x590
-  __DATA_CONST.__cfstring: 0x21c0
+  __DATA_CONST.__cfstring: 0x2300
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x20
+  __DATA_CONST.__objc_arraydata: 0x40
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x4a0
-  __DATA.__objc_selrefs: 0xa88
+  __DATA.__objc_selrefs: 0xab8
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x4ae
   __DATA.__common: 0x468
-  __DATA.__bss: 0xcd
+  __DATA.__bss: 0xd5
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libodfde.dylib
-  UUID: 663D3E1F-E537-329E-AB91-76E63372F88B
-  Functions: 692
-  Symbols:   372
-  CStrings:  2703
+  UUID: 0B5456B7-C346-3DA0-954D-8F6BF3697982
+  Functions: 701
+  Symbols:   379
+  CStrings:  2758
 
Symbols:
+ _CP_GetBootstrapTokenWithOptions
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSThread
+ ___kCFBooleanTrue
+ _kODAttributeTypeMetaNodeLocation
+ _kODAttributeTypeOriginalNodeName
CStrings:
+ "%@: Attempting to grant SecureToken for: %@ (MT: %@)"
+ "%@: Authenticating with local node using Bootstrap Token failed ==> %@"
+ "%@: Failed to get Bootstrap Token ==> %@"
+ "%@: Granting SecureToken to '%@' failed ==> %@"
+ "%@: No password provided for user (%@)"
+ "%@: Requesting Secure Token from OD for: %@"
+ "%@: Unable to get local node ==> %@"
+ "%@: user (%@) already has SecureToken"
+ "%@: user (%@) is not local"
+ "%@: user password is null"
+ "%@: user short name is null"
+ "%@: userRecord is null"
+ "/AppleInternal/Library/BuildRoots/4~CE7sugBjbh9IrZjL_x1SldUdCp4G-VVMpcU4ZXc/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/4~CE7sugBjbh9IrZjL_x1SldUdCp4G-VVMpcU4ZXc/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/4~CE7sugBjbh9IrZjL_x1SldUdCp4G-VVMpcU4ZXc/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/Local/Default"
+ "20:38:37"
+ "AdjustSecureToken"
+ "Enabled"
+ "Jan  4 2026"
+ "MCX.AdjustSecureToken"
+ "Reason"
+ "Recordname"
+ "SecureTokenSupport"
+ "SkipLocalPolicyUpdate"
+ "customFunction:payload:error:"
+ "fdesetup: Setup Assistant appears to be running AND we aren't doing a defer enabling AND we do not have a preconfigured account."
+ "fdesetup: Successfully configured SecureToken for existing account."
+ "firstObject"
+ "isMainThread"
+ "no"
+ "nodeName"
+ "nodeWithSession:name:error:"
+ "setCredentialsWithBootstrapToken:error:"
+ "yes"
- "/AppleInternal/Library/BuildRoots/4~CDx8ugBeyqHgK710ZFOrCfyqbhUExcjm8CcUfFI/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/4~CDx8ugBeyqHgK710ZFOrCfyqbhUExcjm8CcUfFI/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/4~CDx8ugBeyqHgK710ZFOrCfyqbhUExcjm8CcUfFI/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "05:31:08"
- "Dec  5 2025"

```
