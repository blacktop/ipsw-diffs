## DADaemonSupport

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport`

```diff

-2708.2.3.0.0
-  __TEXT.__text: 0x36858
-  __TEXT.__objc_methlist: 0x25e4
+2708.3.2.0.0
+  __TEXT.__text: 0x36e0c
+  __TEXT.__objc_methlist: 0x25ec
   __TEXT.__const: 0x132
   __TEXT.__gcc_except_tab: 0x74c
-  __TEXT.__oslogstring: 0x65cb
-  __TEXT.__cstring: 0x1444
-  __TEXT.__unwind_info: 0xdc8
+  __TEXT.__oslogstring: 0x66f0
+  __TEXT.__cstring: 0x1461
+  __TEXT.__unwind_info: 0xdd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2078
+  __DATA_CONST.__objc_selrefs: 0x2098
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0xb50
+  __DATA_CONST.__got: 0xb98
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0xe80
+  __AUTH_CONST.__cfstring: 0xea0
   __AUTH_CONST.__objc_const: 0x5ba0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 958
-  Symbols:   2118
-  CStrings:  539
+  Functions: 959
+  Symbols:   2126
+  CStrings:  544
 
Symbols:
+ -[DADClient _handleCalDAVServerSimulatorResourceRequest:eventDict:]
+ _OBJC_CLASS_$_NSData
+ _kDAEServerSimulatorActionFetchResource
+ _kDAEServerSimulatorActionPutResource
+ _kDAEServerSimulatorCollectionDefaultCalendar
+ _kDAEServerSimulatorCollectionInbox
+ _kDAEServerSimulatorCollectionKey
+ _kDAEServerSimulatorResourceContentsKey
+ _kDAEServerSimulatorResourceNameKey
+ _kDAEServerSimulatorUsernameKey
+ _xpc_dictionary_set_data
- ___30-[DADClient _dispatchMessage:]_block_invoke_42
- ___30-[DADClient _dispatchMessage:]_block_invoke_43
- ___30-[DADClient _dispatchMessage:]_block_invoke_44
Functions:
~ -[DADClient _manageCalDAVServerSimulatorWithHostname:action:] : 484 -> 528
+ -[DADClient _handleCalDAVServerSimulatorResourceRequest:eventDict:]
~ -[DADClient _dispatchMessage:] : 8676 -> 8692
~ ___30-[DADClient _dispatchMessage:]_block_invoke_41 : 124 -> 336
~ ___35+[DADClient permissionsForMessage:]_block_invoke : 1004 -> 1028
CStrings:
+ "CalDAV server simulator message with unrecognized action: %@"
+ "CalDAV server simulator request for a hostname this client didn't begin: %@"
+ "CalDAV server simulator resource request was sent without a reply"
+ "Malformed CalDAV server simulator request: action %@, collection %@"
+ "_manageCalDAVServerSimulatorWithHostname called with a missing or invalid hostname"
+ "_manageCalDAVServerSimulatorWithHostname called with a non-simulated hostname: %@"
+ "simulated.calendar.apple.com"
- "_manageCalDAVServerSimulatorWithHostname called with nil hostname"
- "_manageCalDAVServerSimulatorWithHostname called with unrecognized action: %@"
```
