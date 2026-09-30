## centaurid

> `/usr/libexec/centaurid`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__data`

```diff

-128.0.0.0.0
-  __TEXT.__text: 0x30788
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_stubs: 0x3560
-  __TEXT.__objc_methlist: 0x115c
+129.0.0.0.0
+  __TEXT.__text: 0x350d0
+  __TEXT.__auth_stubs: 0xaa0
+  __TEXT.__objc_stubs: 0x3bc0
+  __TEXT.__objc_methlist: 0x13e4
   __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x15f0
-  __TEXT.__cstring: 0x19ba3
-  __TEXT.__oslogstring: 0x5d62
-  __TEXT.__objc_methname: 0x33b6
-  __TEXT.__objc_classname: 0x190
-  __TEXT.__objc_methtype: 0x99c
-  __TEXT.__unwind_info: 0xad8
-  __DATA_CONST.__const: 0x7a8
-  __DATA_CONST.__cfstring: 0x10cc0
-  __DATA_CONST.__objc_classlist: 0x78
+  __TEXT.__gcc_except_tab: 0x1730
+  __TEXT.__cstring: 0x1a222
+  __TEXT.__oslogstring: 0x6333
+  __TEXT.__objc_methname: 0x3994
+  __TEXT.__objc_classname: 0x1f2
+  __TEXT.__objc_methtype: 0xaca
+  __TEXT.__unwind_info: 0xbb8
+  __DATA_CONST.__const: 0x880
+  __DATA_CONST.__cfstring: 0x11400
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0xa1e0
-  __DATA_CONST.__objc_arrayobj: 0x5a0
+  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_arraydata: 0xa238
+  __DATA_CONST.__objc_arrayobj: 0x5d0
   __DATA_CONST.__objc_intobj: 0x94b0
   __DATA_CONST.__objc_dictobj: 0x1c48
-  __DATA_CONST.__auth_got: 0x558
-  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__auth_got: 0x568
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x1c40
-  __DATA.__objc_selrefs: 0xe70
-  __DATA.__objc_ivar: 0x1bc
-  __DATA.__objc_data: 0x4b0
+  __DATA.__objc_const: 0x20f8
+  __DATA.__objc_selrefs: 0x1008
+  __DATA.__objc_ivar: 0x1ec
+  __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x2a8
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 629
-  Symbols:   243
-  CStrings:  3511
+  Functions: 697
+  Symbols:   248
+  CStrings:  3677
 
Symbols:
+ _CentauriControllerPortOff
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSError
+ _objc_setProperty_nonatomic_copy
CStrings:
+ "\""
+ "%02x"
+ "%@ (%@)"
+ "%{public}@::%{public}@: address overflow for %{public}@"
+ "%{public}@::%{public}@: crashlog schema plist missing or invalid '%{public}@' key"
+ "%{public}@::%{public}@: decoded %@:%@ is not a valid JSON object; skipping"
+ "%{public}@::%{public}@: decoded proprietary crashlog for %{public}@ is not a valid JSON object; skipping"
+ "%{public}@::%{public}@: exception decoding proprietary crashlog for %{public}@: %@"
+ "%{public}@::%{public}@: exception initializing custom decoder for %{public}@: %@"
+ "%{public}@::%{public}@: failed to decode proprietary crashlog for %{public}@"
+ "%{public}@::%{public}@: failed to decode section %@ for core %@: %@"
+ "%{public}@::%{public}@: failed to decode struct %{public}@ (core %{public}@) at offset %lu of %lu bytes: %{public}@"
+ "%{public}@::%{public}@: failed to initialize wifi crashlog schema parser from %{public}@"
+ "%{public}@::%{public}@: failed to load crashlog schema plist from %{public}@"
+ "%{public}@::%{public}@: failed to turn port off after LPM entry: 0x%08x"
+ "%{public}@::%{public}@: missing or non-dictionary struct %@ in decoded dictionary"
+ "%{public}@::%{public}@: missing or non-numeric aslr_offset"
+ "%{public}@::%{public}@: no crashlog structs found for core %@"
+ "%{public}@::%{public}@: no schema found for struct %@ (core %@)"
+ "%{public}@::%{public}@: non-numeric address value for %{public}@"
+ "%{public}@::%{public}@: port off failed: 0x%08x"
+ "%{public}@::%{public}@: slide greater than address for %{public}@"
+ "%{public}@::%{public}@: unsupported version %lu for unsliding"
+ "'([^']+)'\\s*:\\s*(-?\\d+)"
+ "/tmp/Centauri/wifi-crashlog-schema.plist"
+ ":"
+ "<invalid UTF-8>"
+ "@\"NSArray\"16@0:8"
+ "@\"NSDictionary\"32@0:8@\"NSData\"16@\"NSString\"24"
+ "@\"NSString\"24@0:8@\"NSString\"16"
+ "@\"WiFiCrashlogSchemaPlistParser\""
+ "@32@0:8@16^@24"
+ "@48@0:8@16@24@32^@40"
+ "@48@0:8r*16Q24q32^@40"
+ "@56@0:8r*16Q24@32@40^@48"
+ "@56@0:8r*16Q24q32q40^@48"
+ "@60@0:8r*16Q24q32q40B48^@52"
+ "@64@0:8@16Q24@32@40^Q48^@56"
+ "AppleCentauri-129"
+ "BT-RTKit-Custom-Sections"
+ "ByteArray field exceeds payload bounds"
+ "ByteArray field offset %ld bits is not byte-aligned"
+ "CORE_INFRA_ERROR_dynamic_db_t"
+ "DecodeProprietaryCoreCrashlog"
+ "Dynamic field has negative offset"
+ "Dynamic field offset %ld bits is not byte-aligned"
+ "Dynamic field offset exceeds payload bounds"
+ "Field exceeds payload bounds: need %ld bytes, have %lu"
+ "Field size %ld bits exceeds 64-bit maximum"
+ "Field size %ld bits is invalid"
+ "FieldDefinition"
+ "Invalid schema format - expected struct field definitions: [(type,name,extra,offset,size,signed),...]"
+ "Negative offset or size in schema"
+ "No field definitions found in struct schema"
+ "Offset + size overflow"
+ "PHY_CORE_INFRA_ERROR_dynamic_db_t"
+ "Payload is empty"
+ "Payload too small: schema expects %lu bytes at offset %lu but payload is %lu bytes"
+ "Payload too small: schema expects %lu bytes but payload is %lu bytes"
+ "Q24@0:8@16"
+ "Schema describes a zero-size struct"
+ "Schema is empty"
+ "String field exceeds payload bounds"
+ "String field offset %ld bits is not byte-aligned"
+ "Struct nesting depth exceeds maximum"
+ "T@\"NSString\",C,N,V_extraInfo"
+ "T@\"NSString\",C,N,V_name"
+ "TB,N,V_isSigned"
+ "Tq,N,V_offsetBits"
+ "Tq,N,V_sizeBits"
+ "Tq,N,V_type"
+ "Unmatched EndStruct in schema"
+ "WFL2G"
+ "WFL5G"
+ "WFMAIN"
+ "WFP2G"
+ "WFP5G"
+ "WFRX"
+ "WFSC"
+ "WFTX"
+ "WiFi-RTKit-Custom-Sections"
+ "WiFiCrashlogDecoder"
+ "WiFiCrashlogSchemaPlistParser"
+ "WiFiCrashlogSchemaStructDecoder"
+ "WiFiCrashlogSchemaStructDecoderErrorDomain"
+ "\\(\\s*(\\d+)\\s*,\\s*['\"]?([^',\"]+)['\"]?\\s*,\\s*['\"]?([^',\"]*)['\"]?\\s*,\\s*(\\d+)\\s*,\\s*(\\d+)\\s*,\\s*(\\d+)\\s*\\)"
+ "]"
+ "__proprietaryCoreCrashlogData"
+ "_crashlogStructs"
+ "_enums"
+ "_extraInfo"
+ "_isSigned"
+ "_name"
+ "_offsetBits"
+ "_rtKitEnums"
+ "_rtKitSections"
+ "_schemaParser"
+ "_sizeBits"
+ "_structs"
+ "_type"
+ "aslr_offset"
+ "back_trace"
+ "backtrace"
+ "crashlogStructsForCore:"
+ "crashlog_structs"
+ "decodeData:fromProprietaryCore:"
+ "decodeFieldsFromBytes:length:fields:enumMap:error:"
+ "decodePayload:atOffset:withSchema:withEnumMap:bytesConsumed:error:"
+ "decodePayload:withSchema:withEnumMap:error:"
+ "dictionaryWithCapacity:"
+ "dictionaryWithContentsOfFile:"
+ "enums"
+ "errorWithDomain:code:userInfo:"
+ "extraInfo"
+ "extractBytesFromBytes:length:offsetBits:sizeBits:error:"
+ "extractDynamicFromBytes:length:offsetBits:error:"
+ "extractNumberFromBytes:length:offsetBits:sizeBits:isSigned:error:"
+ "extractStringFromBytes:length:offsetBits:sizeBits:error:"
+ "failed to turn port off after LPM entry: 0x%08x"
+ "info-source"
+ "initWithBytes:length:encoding:"
+ "initWithPlistPath:"
+ "isSigned"
+ "isValidJSONObject:"
+ "lastObject"
+ "lr1"
+ "lr2"
+ "matchesInString:options:range:"
+ "numberWithLongLong:"
+ "offsetBits"
+ "parseEnumString:"
+ "parseEnumsSection:"
+ "parseRTKitSections:"
+ "parseStructFieldsDef:error:"
+ "parseStructsSection:"
+ "parseTraceInfoSchema:error:"
+ "portOff"
+ "proprietaryEnumMap"
+ "removeLastObject"
+ "rtKitCrashlogSchemaForSection:"
+ "rtKitCrashlogSectionNames"
+ "rtKitEnumMap"
+ "rtkit_crashlog_sections"
+ "s_cortex_regs"
+ "setExtraInfo:"
+ "setIsSigned:"
+ "setName:"
+ "setOffsetBits:"
+ "setSizeBits:"
+ "setType:"
+ "sizeBits"
+ "sourceIdentifierForCore:"
+ "sp"
+ "stringByTrimmingCharactersInSet:"
+ "stringWithCapacity:"
+ "structSchemaForName:"
+ "structSizeForFields:"
+ "struct_content"
+ "structs"
+ "supportedProprietaryCores"
+ "unslideAddresses:"
+ "unslideAddressesInDict:slide:"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
+ "whitespaceAndNewlineCharacterSet"
+ "{"
+ "}"
- "AppleCentauri-128"
```
