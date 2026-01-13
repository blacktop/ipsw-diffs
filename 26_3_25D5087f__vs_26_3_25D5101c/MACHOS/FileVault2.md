## FileVault2

> `/System/Library/CoreServices/ManagedClient.app/Contents/PlugIns/FileVault2.profileDomainPlugin/Contents/MacOS/FileVault2`

```diff

-1798.80.2.0.0
-  __TEXT.__text: 0x5b40
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_stubs: 0x940
+1798.80.3.0.0
+  __TEXT.__text: 0x6690
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_stubs: 0xb00
   __TEXT.__objc_methlist: 0xa4
-  __TEXT.__cstring: 0x2570
-  __TEXT.__const: 0x60
-  __TEXT.__oslogstring: 0xebb
+  __TEXT.__cstring: 0x2805
+  __TEXT.__const: 0x78
+  __TEXT.__oslogstring: 0x1094
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__objc_methname: 0x831
+  __TEXT.__objc_methname: 0x97f
   __TEXT.__objc_classname: 0x20
   __TEXT.__objc_methtype: 0xbc
   __TEXT.__unwind_info: 0x160
-  __DATA_CONST.__auth_got: 0x348
-  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_got: 0x360
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x130
-  __DATA_CONST.__cfstring: 0x1280
+  __DATA_CONST.__cfstring: 0x1400
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_arraydata: 0x20
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x298
+  __DATA.__objc_selrefs: 0x308
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x8
   __DATA.__common: 0x150
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x90
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/OpenDirectory.framework/Versions/A/OpenDirectory
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SecurityFoundation.framework/Versions/A/SecurityFoundation
   - /System/Library/PrivateFrameworks/ConfigurationProfiles.framework/Versions/A/ConfigurationProfiles

   - /usr/lib/libCoreStorage.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C9A3107-8A58-3761-8775-C73525080886
-  Functions: 89
-  Symbols:   144
-  CStrings:  566
+  UUID: 07A7347C-34CD-3D4E-9DE9-99FBAB1CB2DE
+  Functions: 97
+  Symbols:   156
+  CStrings:  629
 
Symbols:
+ _CP_GetBootstrapTokenWithOptions
+ _CP_ProfileInstalledFromUserApprovedManagementService
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_ODNode
+ _OBJC_CLASS_$_ODSession
+ ___kCFBooleanTrue
+ __os_log_error_impl
+ _kODAttributeTypeMetaNodeLocation
+ _kODAttributeTypeOriginalNodeName
+ _kODRecordTypeUsers
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
+ "/Local/Default"
+ ";SecureToken;"
+ "AdjustSecureToken"
+ "Enabled"
+ "MCX.AdjustSecureToken"
+ "Reason"
+ "Recordname"
+ "SecureTokenSupport"
+ "SkipLocalPolicyUpdate"
+ "arrayWithObjects:count:"
+ "code"
+ "customFunction:payload:error:"
+ "defaultSession"
+ "dictionaryWithObjects:forKeys:count:"
+ "dsAttrTypeStandard:AuthenticationAuthority"
+ "firstObject"
+ "i"
+ "isMainThread"
+ "no"
+ "nodeName"
+ "nodeWithSession:name:error:"
+ "nodeWithSession:type:error:"
+ "rangeOfString:options:"
+ "recordWithRecordType:name:attributes:error:"
+ "setCredentialsWithBootstrapToken:error:"
+ "valuesForAttribute:error:"
+ "yes"

```
