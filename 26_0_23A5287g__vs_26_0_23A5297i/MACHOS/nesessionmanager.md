## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-2186.0.0.0.0
-  __TEXT.__text: 0xaf5cc
-  __TEXT.__auth_stubs: 0x1cd0
-  __TEXT.__objc_stubs: 0x7fa0
-  __TEXT.__objc_methlist: 0x3cfc
-  __TEXT.__const: 0x178
-  __TEXT.__gcc_except_tab: 0x21a4
-  __TEXT.__objc_methname: 0x9119
-  __TEXT.__oslogstring: 0xee0e
-  __TEXT.__cstring: 0x5150
+2191.0.0.0.0
+  __TEXT.__text: 0xaf608
+  __TEXT.__auth_stubs: 0x1ce0
+  __TEXT.__objc_stubs: 0x7fe0
+  __TEXT.__objc_methlist: 0x3d34
+  __TEXT.__const: 0x188
+  __TEXT.__gcc_except_tab: 0x22b0
+  __TEXT.__objc_methname: 0x90fd
+  __TEXT.__oslogstring: 0xee4b
+  __TEXT.__cstring: 0x5161
   __TEXT.__objc_classname: 0xbac
   __TEXT.__objc_methtype: 0x20b5
   __TEXT.__unwind_info: 0x1610
-  __DATA_CONST.__auth_got: 0xe78
+  __DATA_CONST.__auth_got: 0xe80
   __DATA_CONST.__got: 0x778
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1d58
+  __DATA_CONST.__const: 0x1d08
   __DATA_CONST.__cfstring: 0x26e0
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_protolist: 0x148

   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x8008
-  __DATA.__objc_selrefs: 0x2388
-  __DATA.__objc_ivar: 0x780
+  __DATA.__objc_const: 0x7ff0
+  __DATA.__objc_selrefs: 0x2398
+  __DATA.__objc_ivar: 0x77c
   __DATA.__objc_data: 0x1860
   __DATA.__data: 0xf80
   __DATA.__bss: 0x130

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1B5D8A8D-A7C7-336B-9D26-8D33AC98CAFE
-  Functions: 1861
-  Symbols:   685
-  CStrings:  4290
+  UUID: 091B9A14-CC64-30BF-A4E4-111FBEEA8D33
+  Functions: 1862
+  Symbols:   686
+  CStrings:  4292
 
Symbols:
+ _unlink
CStrings:
+ "%@ uninstalled hotspot provider policies for [%@]"
+ "%@: %s - Deleted file %s"
+ "%@: %s - Failed to delete file %s: [%d] %s"
+ "%@: %s - fetchPreFilterDataWithCompletion - data <%lu bytes>, file %@, sb_extension <%s>, tag <%@> numberOfBits %d, numberOfHashes %d, murmurSeed %d, error %@"
+ "%@: %s - fetchPreFilterDataWithCompletion - data <%lu bytes>, file %@, sb_extension <%s>, tag <%@>,  numberOfBits %d, numberOfHashes  %d, murmurSeed %d, error %@"
+ "%@: %s - savePrefilterData <%u bytes of data> bits %u hashes %u seed %u - using mmap file %@ tag %@"
+ "-[NEAgentURLFilterExtension savePrefilterData:fileURL:sandboxExtension:numberOfBits:numberOfHashes:murmurSeed:tag:]"
+ "extension started successfully with %zu number of process identities"
+ "fetchPrefilterDataWithTag:completion:"
+ "getFilterTag"
+ "getPrefilterTag"
+ "getTag"
+ "mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:tag:"
+ "v60@?0@\"NSData\"8@\"NSURL\"16@\"NSString\"24@\"NSString\"32I40I44I48@\"NSError\"52"
- "%@: %s - fetchPreFilterDataWithCompletion - data <%lu bytes>, file %@, sb_extension <%s>, numberOfBits %d, numberOfHashes  %d, murmurSeed %d, error %@"
- "%@: %s - fetchPreFilterDataWithCompletion - data <%lu bytes>, file %@, sb_extension <%s>, numberOfBits %d, numberOfHashes %d, murmurSeed %d, error %@"
- "%@: %s - savePrefilterData <%u bytes of data> bits %u hashes %u seed %u - using mmap file %@"
- "%@: found new hotspot providers %@"
- "-[NEAgentURLFilterExtension savePrefilterData:fileURL:sandboxExtension:numberOfBits:numberOfHashes:murmurSeed:]"
- "_currentHotspotProviders"
- "extension started successfully with %lu number of process identities"
- "failed to load current configurations, error: %@"
- "fetchPrefilterDataWithCompletion:"
- "loadConfigurationsWithCompletionQueue:handler:"
- "mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:"
- "v52@?0@\"NSData\"8@\"NSURL\"16@\"NSString\"24I32I36I40@\"NSError\"44"

```
