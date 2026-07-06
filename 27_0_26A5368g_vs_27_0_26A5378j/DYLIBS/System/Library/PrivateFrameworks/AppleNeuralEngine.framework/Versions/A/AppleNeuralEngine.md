## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/Versions/A/AppleNeuralEngine`

```diff

-  __TEXT.__text: 0x5ae34
-  __TEXT.__objc_methlist: 0x2b0c
+  __TEXT.__text: 0x5cd10
+  __TEXT.__objc_methlist: 0x2b8c
   __TEXT.__const: 0x2b8
-  __TEXT.__oslogstring: 0xb49e
-  __TEXT.__cstring: 0x3730
-  __TEXT.__gcc_except_tab: 0x65a8
-  __TEXT.__unwind_info: 0x1368
+  __TEXT.__oslogstring: 0xb7ac
+  __TEXT.__cstring: 0x38bd
+  __TEXT.__gcc_except_tab: 0x67a4
+  __TEXT.__unwind_info: 0x1380
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x19d8
+  __DATA_CONST.__objc_selrefs: 0x1a18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x120
   __DATA_CONST.__got: 0x300
-  __AUTH_CONST.__const: 0xd10
-  __AUTH_CONST.__cfstring: 0x48e0
-  __AUTH_CONST.__objc_const: 0x3c70
+  __AUTH_CONST.__const: 0xd70
+  __AUTH_CONST.__cfstring: 0x4aa0
+  __AUTH_CONST.__objc_const: 0x3cd0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x234
-  __DATA.__data: 0x6e8
+  __AUTH_CONST.__auth_got: 0x598
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_ivar: 0x23c
+  __DATA.__data: 0x710
   __DATA.__bss: 0x178
-  __DATA_DIRTY.__objc_data: 0xa50
+  __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 1751
-  Symbols:   3844
-  CStrings:  1979
+  Functions: 1771
+  Symbols:   3886
+  CStrings:  2024
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[_ANECloneHelper bundleContainsSymlinkAtPath:]
+ +[_ANEHashEncoding _hexStringByFeeding:]
+ +[_ANEHashEncoding hexStringForFileAtPath:]
+ +[_ANEHashEncoding verifyBundleAtPath:expectedHashes:error:]
+ +[_ANESandboxingHelper issueSandboxExtensionForWeights:]
+ +[_ANEStrings largeModelCompilerServiceAccessEntitlement]
+ +[_ANEStrings largeModelCompilerServiceBundleID]
+ -[_ANEInMemoryModel perFileHashes]
+ -[_ANEInMemoryModel setPerFileHashes:]
+ -[_ANEInMemoryModelDescriptor perFileHashes]
+ OBJC_IVAR_$__ANEInMemoryModel._perFileHashes
+ OBJC_IVAR_$__ANEInMemoryModelDescriptor._perFileHashes
+ __43+[_ANEHashEncoding hexStringForFileAtPath:]_block_invoke
+ ___42+[_ANEHashEncoding hexStringForDataArray:]_block_invoke
+ ___43+[_ANEHashEncoding hexStringForFileAtPath:]_block_invoke
+ ___45+[_ANEHashEncoding hexStringForBytes:length:]_block_invoke
+ ___block_descriptor_40_e8_32s_e41_B16?0^{CC_SHA256state_st=[2I][8I][16I]}8l
+ ___block_descriptor_44_e8_32s_e41_B16?0^{CC_SHA256state_st=[2I][8I][16I]}8l
+ ___block_descriptor_48_e41_B16?0^{CC_SHA256state_st=[2I][8I][16I]}8l
+ _close
+ _copyfile
+ _copyfile_state_alloc
+ _copyfile_state_free
+ _kANEFCompilerServiceBundleIdentifierKey
+ _kANEFCompilerServiceRUsageAfterKey
+ _kANEFCompilerServiceRUsageBeforeKey
+ _kANEFInMemoryModelFileHashesKey
+ _kANEFInMemoryModelFileNamesKey
+ _lstat
+ _objc_msgSend$_hexStringByFeeding:
+ _objc_msgSend$bundleContainsSymlinkAtPath:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$hexStringForFileAtPath:
+ _objc_msgSend$issueSandboxExtensionForWeights:
+ _objc_msgSend$perFileHashes
+ _objc_msgSend$setExternConstants:
+ _open
+ _read
- _objc_msgSend$allValues
- _objc_msgSend$copyItemAtPath:toPath:error:
CStrings:
+ "%@: --> Calling copyfile(src:%s, dst:%s, flags:0x%x)"
+ "%@: BEGIN errorIOSurfaceRef=%p errorLength=%llu"
+ "%@: baseAddress=%p IOSurfaceAllocSize=%zu"
+ "%@: bundle entry %@ is a symbolic link; refusing"
+ "%@: contentsOfDirectoryAtPath(%@) failed: %@"
+ "%@: copyfile(%s, %s, %o) FAILED with (%d : %s)"
+ "%@: dataOut.success=%d errorDataSize=%llu programHandle=%llu"
+ "%@: decoded errorDescription=%@"
+ "%@: errorData=%p length=%lu"
+ "%@: hostError=%@ (deserialized from %lu bytes)"
+ "%@: input data length=%lu"
+ "%@: loadModelNewInstance FAILED on host: errorDataSize=%llu errorIOSurfaceRef=%p errorIOSID=%u"
+ "%@: lstat(%@) failed errno=%d"
+ "%@: open(%@) failed errno=%d"
+ "%@: refusing model bundle containing a symbolic link: %@"
+ "B16@?0^{CC_SHA256state_st=[2I][8I][16I]}8"
+ "FileConstants"
+ "Path"
+ "_SBExtension"
+ "assetFileName"
+ "assetTransferUUID"
+ "com.apple.ANELargeModelCompilerService"
+ "com.apple.ANELargeModelCompilerService.allow"
+ "hexStringForFileAtPath: read(%@) failed errno=%d"
+ "kANEFCompilerServiceBundleIdentifierKey"
+ "kANEFCompilerServiceRUsageAfterKey"
+ "kANEFCompilerServiceRUsageBeforeKey"
+ "kANEFInMemoryModelFileHashesKey"
+ "kANEFInMemoryModelFileNamesKey"
+ "modelFilePath"
+ "verifyBundleAtPath"
+ "verifyBundleAtPath: %@ missing or not a directory"
+ "verifyBundleAtPath: hash mismatch for %@ in bundle %@ (TOCTOU?)"
- "%@: --> copying directory (%@, %@)"
- "%@: copy directory (%@, %@) FAILED"

```
