## PackageKit

> `/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit`

```diff

-1525.0.1.0.0
-  __TEXT.__text: 0x897a4
+1525.40.7.0.0
+  __TEXT.__text: 0x89d90
   __TEXT.__objc_methlist: 0x7b34
   __TEXT.__const: 0x390
   __TEXT.__constg_swiftt: 0x188

   __TEXT.__swift5_reflstr: 0x21
   __TEXT.__swift5_fieldmd: 0x5c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__cstring: 0x128f4
-  __TEXT.__gcc_except_tab: 0x1560
+  __TEXT.__cstring: 0x12c22
+  __TEXT.__gcc_except_tab: 0x161c
   __TEXT.__oslogstring: 0x39
   __TEXT.__dof_PackageKi: 0x1ba4
   __TEXT.__unwind_info: 0x2980

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4680
+  __DATA_CONST.__objc_selrefs: 0x4698
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x3c0
   __DATA_CONST.__objc_arraydata: 0x68
   __DATA_CONST.__got: 0x9b8
   __AUTH_CONST.__const: 0x1850
   __AUTH_CONST.__cfstring: 0xbc80
-  __AUTH_CONST.__objc_const: 0xc328
+  __AUTH_CONST.__objc_const: 0xc368
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x10d8
   __AUTH.__objc_data: 0x13d0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xa18
+  __DATA.__objc_ivar: 0xa20
   __DATA.__data: 0x830
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__objc_ivar: 0x48

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 2886
-  Symbols:   7583
-  CStrings:  2155
+  Symbols:   7588
+  CStrings:  2162
 
Symbols:
+ -[PKInstallScriptMutation initWithBaseDirectory:relativeScriptPath:dropSIP:skipScript:mutationToPerform:]
+ OBJC_IVAR_$_PKBOM._needsAFSCCompression
+ OBJC_IVAR_$_PKInstallScriptMutation._baseDirectory
+ OBJC_IVAR_$_PKInstallScriptMutation._relativeScriptPath
+ _objc_msgSend$readDataToEndOfFileAndReturnError:
+ _objc_msgSend$truncateAtOffset:error:
+ _objc_msgSend$writeData:error:
- -[PKInstallScriptMutation initWithScriptPath:dropSIP:skipScript:mutationToPerform:]
- OBJC_IVAR_$_PKInstallScriptMutation._scriptPath
Functions:
~ -[PKInstallRequest _initWithPackages:destination:withOutError:] : 1552 -> 1560
~ -[PKBOM dealloc] : 144 -> 176
~ -[PKMutableBOM commitData] : 88 -> 52
~ -[PKRunPackageScriptInstallOperation _runPackageScript:packageSpecifier:component:scriptName:error:] : 1872 -> 1888
~ ___86-[PKPayloadCopier _startPBlockCompressorWithEncoder:decoder:blockSize:signalWhenDone:]_block_invoke : 484 -> 528
~ -[PKInstallScriptOverrides mutationsMatchingScriptType:scriptsDirectory:packageComponentIdentifier:] : 744 -> 768
~ -[PKInstallScriptMutation initWithScriptPath:dropSIP:skipScript:mutationToPerform:] -> -[PKInstallScriptMutation initWithBaseDirectory:relativeScriptPath:dropSIP:skipScript:mutationToPerform:] : 196 -> 212
~ -[PKInstallScriptMutation dealloc] : 136 -> 148
~ -[PKInstallScriptMutation performMutationWithError:] : 2032 -> 3432
CStrings:
+ "PackageKit: An install script mutation (%s) cannot be performed because it has no target."
+ "PackageKit: An install script mutation (%s) cannot be performed because the scripts directory (%s) could not be opened. %s"
+ "PackageKit: An install script mutation (%s) could not delete the script at path:(%s). %s"
+ "PackageKit: An install script mutation named (%s) cannot be performed because the script at path:(%s) could not be opened. %s"
+ "PackageKit: An install script mutation named (%s) cannot be performed because the script at path:(%s) could not be read. %s"
+ "PackageKit: An install script mutation named (%s) cannot be performed because the script at path:(%s) could not be stat'd. %s"
+ "PackageKit: An install script mutation named (%s) cannot be performed because the script at path:(%s) is not a regular file. (mode:%o)"
+ "PackageKit: An install script mutation named (%s) cannot be performed because the script at path:(%s) is not valid UTF-8."
- "PackageKit: An install script mutation named (%s) cannot be performed because the script does not exist at path:(%s). %s"
```
