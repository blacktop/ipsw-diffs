## NearFieldPrivateServices

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/NearFieldPrivateServices`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0x6c7c
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0x48c
-  __TEXT.__const: 0x90
+366.4.0.0.0
+  __TEXT.__text: 0x81e8
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0x654
+  __TEXT.__const: 0x98
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__cstring: 0x142c
-  __TEXT.__oslogstring: 0x638
-  __TEXT.__unwind_info: 0x190
-  __TEXT.__objc_classname: 0x10f
-  __TEXT.__objc_methname: 0x9ec
-  __TEXT.__objc_methtype: 0x29f
-  __TEXT.__objc_stubs: 0x7e0
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x508
-  __DATA_CONST.__objc_classlist: 0x40
+  __TEXT.__cstring: 0x17a3
+  __TEXT.__oslogstring: 0x6e4
+  __TEXT.__unwind_info: 0x1d0
+  __TEXT.__objc_classname: 0x152
+  __TEXT.__objc_methname: 0xf4b
+  __TEXT.__objc_methtype: 0x37e
+  __TEXT.__objc_stubs: 0xb40
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0x540
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x378
+  __DATA_CONST.__objc_selrefs: 0x4d0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x210
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x580
-  __AUTH_CONST.__objc_const: 0x758
-  __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x1c
+  __DATA_CONST.__objc_superrefs: 0x40
+  __AUTH_CONST.__auth_got: 0x230
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x8e0
+  __AUTH_CONST.__objc_const: 0x9d0
+  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x180
   __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 756E4C9E-45B6-39C0-9950-B1B354FDEEC0
-  Functions: 94
-  Symbols:   102
-  CStrings:  453
+  UUID: 75E4D793-CE9D-32EA-B7D9-12DA497D1B8A
+  Functions: 130
+  Symbols:   116
+  CStrings:  583
 
Symbols:
+ _OBJC_CLASS_$_NFLocation
+ _OBJC_CLASS_$_NFLocationService
+ _OBJC_CLASS_$_NFLocationServiceListener
+ _OBJC_CLASS_$_NFReportingService
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_METACLASS_$_NFLocationService
+ _OBJC_METACLASS_$_NFLocationServiceListener
+ _OBJC_METACLASS_$_NFReportingService
+ ___assert_rtn
+ _objc_retain_x24
+ _objc_retain_x26
+ _objc_storeWeak
- _OBJC_CLASS_$_NSConstantDictionary
CStrings:
+ "!"
+ "%s:%i Disconnect service due to 0 listeners registered"
+ "%s:%i Failed to call into service for operation %@, model %@ : %@"
+ "%s:%i Failed to call into service for operation %@, model %@ : no result.."
+ "%s:%i Listener not found for bundle %{public}@"
+ "%{public}s:%i Disconnect service due to 0 listeners registered"
+ "%{public}s:%i Failed to call into service for operation %@, model %@ : %@"
+ "%{public}s:%i Failed to call into service for operation %@, model %@ : no result.."
+ "%{public}s:%i Listener not found for bundle %{public}@"
+ "-[NFLocationService invalidateListener:]"
+ "-[NFLocationService notifyLocationAuthDenied:]"
+ "-[NFLocationService notifyLocationSimulationDetected:]"
+ "-[NFLocationService notifyLocationUpdate:location:]"
+ "-[NFLocationService startListenerWithBundleIdentifier:delegate:error:]"
+ "-[NFStorageService executeOperation:onModel:withParams:outError:]"
+ "@\"<NFLocationServiceListenerDelegate>\""
+ "@\"NSMutableDictionary\""
+ "@\"NSString\""
+ "@20@0:8B16"
+ "@40@0:8@16@24^@32"
+ "@44@0:8@16@24d32B40"
+ "@48@0:8@16@24@32^@40"
+ "@48@0:8@16@24^d32^B40"
+ "@64@0:8@16@24Q32@40^@48^B56"
+ "CoreNFCUI_Access"
+ "CoreNFCUI_ScanMode"
+ "Delete"
+ "DeveloperPresentment"
+ "DeveloperPresentmentReceipt"
+ "Location service is not authorized"
+ "Location simulation detected"
+ "NFLocationService"
+ "NFLocationService.m"
+ "NFLocationServiceListener"
+ "NFReportingService"
+ "Params"
+ "TB,N,V_isStarted"
+ "UUIDString"
+ "User has denied access to location services"
+ "_bundleIdentifier"
+ "_delegate"
+ "_isStarted"
+ "_listenerMap"
+ "_lock"
+ "action"
+ "authDenied"
+ "begin"
+ "bundleID"
+ "com.apple.stockholm.services.NFLocationService"
+ "com.apple.stockholm.services.NFReportingService"
+ "configureExportedInterface:"
+ "configureRemoteObjectInterface:"
+ "configureReporter"
+ "configureReporterWithSEKeying:"
+ "coreNFCUISetAccess:"
+ "coreNFCUISetScanMode:"
+ "deleteAllDeveloperPaymentReports"
+ "deleteAllReportReceipts"
+ "deleteDeveloperPaymentReportWithID:"
+ "doubleValue"
+ "executeOperation:onModel:withParams:outError:"
+ "exportedInterface"
+ "fetchDeveloperPaymentReportWithID:outError:"
+ "fetchDeveloperPaymentReportsWithError:"
+ "getLastReportReceiptForBundleID:teamID:outSentTimestamp:outIsOnDenyList:"
+ "httpStatusCode"
+ "i32@0:8@16^@24"
+ "initWithObjects:"
+ "initWithUUIDString:"
+ "intValue"
+ "invalidateListener:"
+ "isOnDenyList"
+ "isProdSE"
+ "isStarted"
+ "lastSentTimestamp"
+ "listenerStartedWithBundleIdentifier:"
+ "location"
+ "locationAuthDenied:"
+ "locationSimulated"
+ "locationSimulationDetected:"
+ "locationUpdate"
+ "locationUpdated:location:"
+ "nil != bundleIdentifier"
+ "nil != listener"
+ "notifyListenerStarted"
+ "notifyLocationAuthDenied"
+ "notifyLocationAuthDenied:"
+ "notifyLocationSimulationDetected"
+ "notifyLocationSimulationDetected:"
+ "notifyLocationUpdate:"
+ "notifyLocationUpdate:location:"
+ "numberWithBool:"
+ "numberWithUnsignedLongLong:"
+ "objectForKeyedSubscript:"
+ "presentmentData"
+ "remoteObjectInterface"
+ "removeObjectForKey:"
+ "reportData"
+ "reportID"
+ "reportReadyToSend"
+ "saveDeveloperPaymentPresentmentWithBundleID:teamID:timestampDay:presentmentData:savedToReport:reportReadyToSend:"
+ "sendReport"
+ "sendReport:outError:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setIsStarted:"
+ "setObject:forKey:"
+ "startListenerWithBundleIdentifier:delegate:error:"
+ "teamID"
+ "timestampDay"
+ "updatePresentmentReportReceiptWithBundleID:teamID:sentTimestamp:isOnDenyList:"
+ "v32@0:8@16@24"
- "%s:%i Failed to call into service : %@"
- "%s:%i Failed to call into service : no result.."
- "%{public}s:%i Failed to call into service : %@"
- "%{public}s:%i Failed to call into service : no result.."
- "-[NFStorageService deleteAllAppletEntities]"
- "-[NFStorageService deleteAllESEExpressEntities]"
- "-[NFStorageService updateAppletEntitiesWithConfig:]"
- "-[NFStorageService updateESEExpressEntitiesWithConfig:]"
- "Config"

```
