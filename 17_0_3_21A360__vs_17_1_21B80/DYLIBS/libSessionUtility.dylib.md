## libSessionUtility.dylib

> `/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib`

```diff

-263.1.8.30.2
-  __TEXT.__text: 0x352ac
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__cstring: 0x1397
-  __TEXT.__gcc_except_tab: 0x1ff0
+263.2.7.0.0
+  __TEXT.__text: 0x35568
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_methlist: 0xa4
+  __TEXT.__cstring: 0x13f9
+  __TEXT.__gcc_except_tab: 0x2034
   __TEXT.__const: 0x54
-  __TEXT.__unwind_info: 0x18bc
+  __TEXT.__unwind_info: 0x18e0
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0xbc
-  __TEXT.__objc_methname: 0x663
-  __TEXT.__objc_methtype: 0x718
-  __TEXT.__objc_stubs: 0xa0
+  __TEXT.__objc_classname: 0xf6
+  __TEXT.__objc_methname: 0x8a0
+  __TEXT.__objc_methtype: 0x80c
+  __TEXT.__objc_stubs: 0x160
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x98
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4d8
-  __DATA_CONST.__objc_selrefs: 0x60
-  __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__objc_const: 0x698
+  __DATA_CONST.__objc_selrefs: 0xf8
+  __AUTH_CONST.__cfstring: 0x200
+  __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__auth_got: 0x218
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x70
-  __DATA.__data: 0x1e8
+  __DATA.__objc_superrefs: 0x8
+  __DATA.__objc_ivar: 0x10
+  __DATA.__data: 0x2a8
   __DATA.__common: 0x8
   __DATA.__bss: 0x2c0
   __DATA_DIRTY.__const: 0xb80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D75F6454-2871-30F0-BCAB-8B2F8703BD5F
-  Functions: 1362
-  Symbols:   2370
-  CStrings:  381
+  UUID: 6D58BD73-170B-3733-BAEB-A7527EB57505
+  Functions: 1374
+  Symbols:   2434
+  CStrings:  437
 
Symbols:
+ +[AVAudioApplicationSpecification supportsSecureCoding]
+ -[AVAudioApplicationSpecification .cxx_destruct]
+ -[AVAudioApplicationSpecification appAuditToken]
+ -[AVAudioApplicationSpecification attributionBundleID]
+ -[AVAudioApplicationSpecification audioAppType]
+ -[AVAudioApplicationSpecification encodeWithCoder:]
+ -[AVAudioApplicationSpecification initWithCoder:]
+ -[AVAudioApplicationSpecification processName]
+ -[AVAudioApplicationSpecification setAppAuditToken:]
+ -[AVAudioApplicationSpecification setAttributionBundleID:]
+ -[AVAudioApplicationSpecification setAudioAppType:]
+ -[AVAudioApplicationSpecification setProcessName:]
+ _OBJC_CLASS_$_AVAudioApplicationSpecification
+ _OBJC_CLASS_$_NSObject
+ _OBJC_IVAR_$_AVAudioApplicationSpecification._appAuditToken
+ _OBJC_IVAR_$_AVAudioApplicationSpecification.attributionBundleID
+ _OBJC_IVAR_$_AVAudioApplicationSpecification.audioAppType
+ _OBJC_IVAR_$_AVAudioApplicationSpecification.processName
+ _OBJC_METACLASS_$_AVAudioApplicationSpecification
+ _OBJC_METACLASS_$_NSObject
+ __OBJC_$_CLASS_METHODS_AVAudioApplicationSpecification
+ __OBJC_$_CLASS_PROP_LIST_AVAudioApplicationSpecification
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_AVAudioApplicationSpecification
+ __OBJC_$_INSTANCE_VARIABLES_AVAudioApplicationSpecification
+ __OBJC_$_PROP_LIST_AVAudioApplicationSpecification
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_AVAudioApplicationSpecification
+ __OBJC_CLASS_RO_$_AVAudioApplicationSpecification
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_AVAudioApplicationSpecification
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __objc_empty_cache
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$getBytes:length:
+ _objc_msgSendSuper2
+ _objc_release
+ _objc_release_x21
+ _objc_release_x8
+ _objc_retain_x2
CStrings:
+ "\x12"
+ ".cxx_destruct"
+ "@\"NSString\""
+ "@16@0:8"
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8@16"
+ "AVAudioApplicationSpecification"
+ "B16@0:8"
+ "NSCoding"
+ "NSSecureCoding"
+ "PrefersConcurrentAirPlayAudioDidChange"
+ "T@\"NSString\",&,N,VattributionBundleID"
+ "T@\"NSString\",&,N,VprocessName"
+ "TB,R"
+ "Tq,N,VaudioAppType"
+ "T{?=[8I]},N,V_appAuditToken"
+ "_appAuditToken"
+ "allowAppToInitiatePlaybackTemporarilyFromBackground:reply:"
+ "appAuditToken"
+ "attributionBundleID"
+ "audioAppType"
+ "dataWithBytes:length:"
+ "decodeIntegerForKey:"
+ "decodeObjectOfClass:forKey:"
+ "encodeInteger:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "getBytes:length:"
+ "init"
+ "initWithCoder:"
+ "processName"
+ "q"
+ "q16@0:8"
+ "setAppAuditToken:"
+ "setAttributionBundleID:"
+ "setAudioAppType:"
+ "setProcessName:"
+ "setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:"
+ "setSessionPlayState:playState:playerType:playerRef:modes:reply:"
+ "supportsSecureCoding"
+ "v16@0:8"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@16"
+ "v24@0:8q16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v48@0:8I16@\"NSDictionary\"20B28i32B36@?<v@?@\"NSError\"@\"NSArray\">40"
+ "v48@0:8I16@20B28i32B36@?40"
+ "v48@0:8I16I20I24@\"NSString\"28I36@?<v@?@\"NSError\">40"
+ "v48@0:8I16I20I24@28I36@?40"
+ "v48@0:8{?=[8I]}16"
+ "{?=\"val\"[8I]}"
+ "{?=[8I]}16@0:8"
- "setMXPropertyGenericPipe:values:reply:"
- "setProperties:values:MXProperties:batchStrategy:reply:"
- "v36@0:8I16@\"NSDictionary\"20@?<v@?@\"NSError\">28"
- "v44@0:8I16@\"NSDictionary\"20B28i32@?<v@?@\"NSError\"@\"NSArray\">36"
- "v44@0:8I16@20B28i32@?36"

```
