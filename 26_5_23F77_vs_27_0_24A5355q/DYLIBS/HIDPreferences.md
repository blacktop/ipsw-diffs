## HIDPreferences

> `/System/Library/PrivateFrameworks/HIDPreferences.framework/HIDPreferences`

```diff

-2238.120.5.0.0
-  __TEXT.__text: 0x4714
-  __TEXT.__auth_stubs: 0x420
+2353.0.0.0.1
+  __TEXT.__text: 0x4308
   __TEXT.__objc_methlist: 0x35c
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x1f8
   __TEXT.__oslogstring: 0xaf0
-  __TEXT.__cstring: 0xde
+  __TEXT.__cstring: 0xe7
   __TEXT.__unwind_info: 0x188
-  __TEXT.__objc_classname: 0x84
-  __TEXT.__objc_methname: 0x431
-  __TEXT.__objc_methtype: 0x34b
-  __TEXT.__objc_stubs: 0x3a0
-  __DATA_CONST.__got: 0x68
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x220
+  __DATA_CONST.__got: 0x68
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0xd40
   __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5776A8BB-0BFC-3B5A-9CFC-5A72EDAC8B81
-  Functions: 121
-  Symbols:   478
-  CStrings:  185
+  UUID: 1676570D-C160-3D25-90C5-04BB54D78A05
+  Functions: 117
+  Symbols:   471
+  CStrings:  81
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_12
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"HIDPreferencesHelperListener\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "HIDPreferences"
- "HIDPreferencesHelperClient"
- "HIDPreferencesHelperListener"
- "HIDPreferencesLocal"
- "HIDPreferencesProtocol"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_clients"
- "_connection"
- "_listener"
- "_option"
- "_queue"
- "acceptConnection:onQueue:"
- "addObject:"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "containsObject:"
- "copy:user:host:domain:reply:"
- "copyDomain:domain:reply:"
- "copyMultiple:user:host:domain:reply:"
- "count"
- "dealloc"
- "debugDescription"
- "description"
- "destroyConnection:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "enumerateKeysAndObjectsUsingBlock:"
- "getReply:"
- "handleMessage:"
- "hash"
- "i"
- "init"
- "initWithConnection:listener:onQueue:"
- "initWithOption:"
- "integerValue"
- "invalidateConnection"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "removeClient:"
- "removeObject:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "set:value:user:host:domain:"
- "setDomain:value:domain:"
- "setMultiple:keysToRemove:user:host:domain:"
- "setObject:forKeyedSubscript:"
- "setupConnection"
- "setupConnectionOnQueue:"
- "setupListener"
- "superclass"
- "synchronize:host:domain:"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@>32"
- "v40@0:8@\"NSString\"16@24@\"NSString\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v56@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@>48"
- "v56@0:8@\"NSDictionary\"16@\"NSArray\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@>48"
- "v56@0:8@\"NSString\"16@24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24@32@40@?48"
- "zone"

```
