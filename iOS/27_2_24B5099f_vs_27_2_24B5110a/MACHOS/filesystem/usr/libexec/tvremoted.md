## tvremoted

> `usr/libexec/tvremoted`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-627.10.51.0.0
-  __TEXT.__text: 0x1107c
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_stubs: 0x2640
-  __TEXT.__objc_methlist: 0xf54
-  __TEXT.__const: 0xca
+627.11.4.0.0
+  __TEXT.__text: 0x121fc
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_stubs: 0x27e0
+  __TEXT.__objc_methlist: 0xfb8
+  __TEXT.__const: 0xea
   __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__cstring: 0xb5d
-  __TEXT.__objc_methname: 0x32e0
-  __TEXT.__oslogstring: 0x2716
+  __TEXT.__cstring: 0xb4a
+  __TEXT.__objc_methname: 0x3494
+  __TEXT.__oslogstring: 0x28ef
   __TEXT.__objc_classname: 0x13d
-  __TEXT.__objc_methtype: 0xf7a
-  __TEXT.__unwind_info: 0x528
-  __DATA_CONST.__const: 0x6c8
-  __DATA_CONST.__cfstring: 0x960
+  __TEXT.__objc_methtype: 0xfe3
+  __TEXT.__unwind_info: 0x548
+  __DATA_CONST.__const: 0x6f0
+  __DATA_CONST.__cfstring: 0xa00
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0x220
-  __DATA.__objc_const: 0xe60
-  __DATA.__objc_selrefs: 0xcd0
-  __DATA.__objc_ivar: 0x7c
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x228
+  __DATA.__objc_const: 0xe98
+  __DATA.__objc_selrefs: 0xd38
+  __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 334
-  Symbols:   164
-  CStrings:  940
+  Functions: 344
+  Symbols:   167
+  CStrings:  970
 
Symbols:
+ _OBJC_CLASS_$_NSMapTable
+ _dispatch_assert_queue$V2
+ _objc_retain_x25
CStrings:
+ "%{public}@ asked for discovery sources %{public}@"
+ "%{public}@ asked to begin device query with discovery sources %{public}@"
+ "%{public}@ joined the running device query, which only covered %{public}@, and asked for %{public}@; widened it to %{public}@"
+ "%{public}@ left the device query; narrowing it from %{public}@ to %{public}@"
+ "(unknown: 0x%lx)"
+ "@\"NSSet\"32@0:8@\"TVRDClientProcessConnection\"16@\"NSString\"24"
+ "@32@0:8Q16@24"
+ "All"
+ "Companion"
+ "HomeKit"
+ "Q"
+ "Sending %lu of %lu discovered device(s) to %{public}@ (discovery sources %{public}@)"
+ "TQ,N,V_discoverySources"
+ "Union of discovery sources across %lu observer(s): %{public}@"
+ "_closeConnectionToDeviceWithIdentifier:withType:"
+ "_discoverySources"
+ "_sendDiscoveredDevices:toConnection:"
+ "_stateForEachDevice:"
+ "_statesMatchingSources:fromStateForDevice:"
+ "_unionDiscoverySourcesForObservers"
+ "addDiscoverySources:"
+ "beginDeviceQueryWithSources:response:"
+ "clientConnection:identifiersForDeviceWithIdentifier:"
+ "componentsJoinedByString:"
+ "discoverySource"
+ "discoverySources"
+ "objectEnumerator"
+ "removeDiscoverySources:"
+ "setDiscoverySources:"
+ "strongToStrongObjectsMapTable"
+ "v24@0:8Q16"
+ "v32@0:8Q16@?24"
+ "v32@0:8Q16@?<v@?B>24"
+ "|"
- "-[TVRDClientProcessConnection beginDeviceQueryWithResponse:]"
- "beginDeviceQueryWithResponse:"
- "setOfStatesFromDevices:"
- "v24@0:8@?<v@?B>16"
```
