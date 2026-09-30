## PhotoFoundation

> `/System/Library/PrivateFrameworks/PhotoFoundation.framework/Versions/A/PhotoFoundation`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x8170
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x8d0
+751.0.104.0.0
+  __TEXT.__text: 0x9998
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_methlist: 0xc24
   __TEXT.__const: 0xb8
   __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__cstring: 0x7e1
-  __TEXT.__oslogstring: 0x33a
-  __TEXT.__unwind_info: 0x2e8
-  __TEXT.__objc_classname: 0x244
-  __TEXT.__objc_methname: 0x1880
-  __TEXT.__objc_methtype: 0x4d3
-  __TEXT.__objc_stubs: 0x13a0
-  __DATA_CONST.__got: 0x148
+  __TEXT.__cstring: 0x853
+  __TEXT.__oslogstring: 0x59f
+  __TEXT.__unwind_info: 0x338
+  __TEXT.__objc_classname: 0x2ac
+  __TEXT.__objc_methname: 0x1b54
+  __TEXT.__objc_methtype: 0x535
+  __TEXT.__objc_stubs: 0x1520
+  __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__objc_classlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_selrefs: 0x7d0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__objc_superrefs: 0x50
+  __AUTH_CONST.__auth_got: 0x328
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x760
-  __AUTH_CONST.__objc_const: 0x1f10
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0xec
-  __DATA.__data: 0x1e0
+  __AUTH_CONST.__cfstring: 0xa20
+  __AUTH_CONST.__objc_const: 0x20d8
+  __AUTH.__objc_data: 0x690
+  __DATA.__objc_ivar: 0x118
+  __DATA.__data: 0x240
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 360491CE-63EF-3DAE-AFD5-F1251C5E880D
-  Functions: 259
-  Symbols:   843
-  CStrings:  571
+  UUID: BD12AC9B-6D61-3EF8-BCC6-E076946EF19F
+  Functions: 321
+  Symbols:   964
+  CStrings:  700
 
Symbols:
+ +[PFAbstractStateCaptureEvent currentThreadID]
+ -[PFAbstractStateCaptureEvent endTimestamp]
+ -[PFAbstractStateCaptureEvent end]
+ -[PFAbstractStateCaptureEvent eventDescription]
+ -[PFAbstractStateCaptureEvent qosClass]
+ -[PFAbstractStateCaptureEvent reset]
+ -[PFAbstractStateCaptureEvent setEndTimestamp:]
+ -[PFAbstractStateCaptureEvent setInitialValues]
+ -[PFAbstractStateCaptureEvent setQosClass:]
+ -[PFAbstractStateCaptureEvent setStartTimestamp:]
+ -[PFAbstractStateCaptureEvent setThreadID:]
+ -[PFAbstractStateCaptureEvent startTimestamp]
+ -[PFAbstractStateCaptureEvent threadID]
+ -[PFStateCaptureEventDescription .cxx_destruct]
+ -[PFStateCaptureEventDescription appendAbsoluteTimestamp:]
+ -[PFStateCaptureEventDescription appendBool:]
+ -[PFStateCaptureEventDescription appendDuration:]
+ -[PFStateCaptureEventDescription appendEndTimestamp:]
+ -[PFStateCaptureEventDescription appendInteger:]
+ -[PFStateCaptureEventDescription appendQoSClass:]
+ -[PFStateCaptureEventDescription appendRelativeTimestamp:]
+ -[PFStateCaptureEventDescription appendString:]
+ -[PFStateCaptureEventDescription appendThreadID:]
+ -[PFStateCaptureEventDescription appendUInt64:]
+ -[PFStateCaptureEventDescription appendUnsignedInteger:]
+ -[PFStateCaptureEventDescription description]
+ -[PFStateCaptureEventDescription initWithStartTimestamp:]
+ -[PFStateCaptureEventDescription startTimestamp]
+ -[PFStateCaptureEventLog .cxx_destruct]
+ -[PFStateCaptureEventLog addEvent]
+ -[PFStateCaptureEventLog count]
+ -[PFStateCaptureEventLog eventDescriptions]
+ -[PFStateCaptureEventLog initWithEventClass:maxEvents:]
+ GCC_except_table109
+ GCC_except_table123
+ GCC_except_table125
+ GCC_except_table174
+ GCC_except_table291
+ GCC_except_table298
+ OBJC_IVAR_$_PFAbstractStateCaptureEvent._endTimestamp
+ OBJC_IVAR_$_PFAbstractStateCaptureEvent._qosClass
+ OBJC_IVAR_$_PFAbstractStateCaptureEvent._startTimestamp
+ OBJC_IVAR_$_PFAbstractStateCaptureEvent._threadID
+ OBJC_IVAR_$_PFStateCaptureEventDescription._description
+ OBJC_IVAR_$_PFStateCaptureEventDescription._startTimestamp
+ OBJC_IVAR_$_PFStateCaptureEventLog._eventClass
+ OBJC_IVAR_$_PFStateCaptureEventLog._lock
+ OBJC_IVAR_$_PFStateCaptureEventLog._lock_events
+ OBJC_IVAR_$_PFStateCaptureEventLog._lock_headIndex
+ OBJC_IVAR_$_PFStateCaptureEventLog._maxEvents
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_PFAbstractStateCaptureEvent
+ _OBJC_CLASS_$_PFStateCaptureEventDescription
+ _OBJC_CLASS_$_PFStateCaptureEventLog
+ _OBJC_METACLASS_$_PFAbstractStateCaptureEvent
+ _OBJC_METACLASS_$_PFStateCaptureEventDescription
+ _OBJC_METACLASS_$_PFStateCaptureEventLog
+ _PFCrashWithErrno
+ _PFCrashWithUnknownErrno
+ _PFCrashWith_EACCES
+ _PFCrashWith_EAGAIN
+ _PFCrashWith_EBADF
+ _PFCrashWith_EBUSY
+ _PFCrashWith_ECONNREFUSED
+ _PFCrashWith_EDEADLK
+ _PFCrashWith_EEXIST
+ _PFCrashWith_EFAULT
+ _PFCrashWith_EFBIG
+ _PFCrashWith_EINTR
+ _PFCrashWith_EINVAL
+ _PFCrashWith_EIO
+ _PFCrashWith_EISDIR
+ _PFCrashWith_ELOOP
+ _PFCrashWith_EMFILE
+ _PFCrashWith_EMLINK
+ _PFCrashWith_ENAMETOOLONG
+ _PFCrashWith_ENFILE
+ _PFCrashWith_ENOENT
+ _PFCrashWith_ENOMEM
+ _PFCrashWith_ENOSPC
+ _PFCrashWith_ENOTDIR
+ _PFCrashWith_EPERM
+ _PFCrashWith_EROFS
+ _PFCrashWith_ESPIPE
+ _PFCrashWith_ETIMEDOUT
+ __OBJC_$_CLASS_METHODS_PFAbstractStateCaptureEvent
+ __OBJC_$_CLASS_PROP_LIST_PFAbstractStateCaptureEvent
+ __OBJC_$_INSTANCE_METHODS_PFAbstractStateCaptureEvent
+ __OBJC_$_INSTANCE_METHODS_PFStateCaptureEventDescription
+ __OBJC_$_INSTANCE_METHODS_PFStateCaptureEventLog
+ __OBJC_$_INSTANCE_VARIABLES_PFAbstractStateCaptureEvent
+ __OBJC_$_INSTANCE_VARIABLES_PFStateCaptureEventDescription
+ __OBJC_$_INSTANCE_VARIABLES_PFStateCaptureEventLog
+ __OBJC_$_PROP_LIST_PFAbstractStateCaptureEvent
+ __OBJC_$_PROP_LIST_PFStateCaptureEventDescription
+ __OBJC_$_PROP_LIST_PFStateCaptureEventLog
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PFStateCaptureEvent
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PFStateCaptureEvent
+ __OBJC_$_PROTOCOL_REFS_PFStateCaptureEvent
+ __OBJC_CLASS_PROTOCOLS_$_PFAbstractStateCaptureEvent
+ __OBJC_CLASS_RO_$_PFAbstractStateCaptureEvent
+ __OBJC_CLASS_RO_$_PFStateCaptureEventDescription
+ __OBJC_CLASS_RO_$_PFStateCaptureEventLog
+ __OBJC_LABEL_PROTOCOL_$_PFStateCaptureEvent
+ __OBJC_METACLASS_RO_$_PFAbstractStateCaptureEvent
+ __OBJC_METACLASS_RO_$_PFStateCaptureEventDescription
+ __OBJC_METACLASS_RO_$_PFStateCaptureEventLog
+ __OBJC_PROTOCOL_$_PFStateCaptureEvent
+ ___error
+ __block_literal_global.116
+ __block_literal_global.120
+ __block_literal_global.3.395
+ __block_literal_global.308
+ __block_literal_global.347
+ __block_literal_global.390
+ __block_literal_global.483
+ __block_literal_global.63
+ __block_literal_global.70
+ __os_crash
+ _objc_autorelease
+ _objc_exception_throw
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendRelativeTimestamp:
+ _objc_msgSend$appendString:
+ _objc_msgSend$currentThreadID
+ _objc_msgSend$eventDescription
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$reset
+ _objc_msgSend$setEndTimestamp:
+ _objc_msgSend$setQosClass:
+ _objc_msgSend$setStartTimestamp:
+ _objc_msgSend$setThreadID:
+ _objc_msgSend$stringFromTimestamp:
+ _pthread_threadid_np
+ _qos_class_self
+ _strerror
- GCC_except_table113
- GCC_except_table230
- GCC_except_table237
- GCC_except_table61
- GCC_except_table75
- GCC_except_table77
- __block_literal_global.14
- __block_literal_global.160
- __block_literal_global.192
- __block_literal_global.21
- __block_literal_global.220
- __block_literal_global.3.225
- __block_literal_global.305
- __block_literal_global.41
- __block_literal_global.44
CStrings:
+ " end: "
+ " now: "
+ "%+.3f"
+ "%0.3f"
+ "%@:"
+ "%@: %s (%d)"
+ "%llu"
+ "%tu"
+ "%zd"
+ "%{public}@: Deallocating with state handle: %llu"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/Projects/PhotoFoundation/Source/PFAssert.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/Projects/PhotoFoundation/Source/PFGeometryUtilities.m"
+ "0x%-8llx"
+ "1"
+ "<nil>"
+ "@\"NSMutableString\""
+ "@20@0:8B16"
+ "@20@0:8I16"
+ "@24@0:8Q16"
+ "@24@0:8q16"
+ "@32@0:8#16Q24"
+ "BG"
+ "Crashing due to EACCES"
+ "Crashing due to EAGAIN"
+ "Crashing due to EBADF"
+ "Crashing due to EBUSY"
+ "Crashing due to ECONNREFUSED"
+ "Crashing due to EDEADLK"
+ "Crashing due to EEXIST"
+ "Crashing due to EFAULT"
+ "Crashing due to EFBIG"
+ "Crashing due to EINTR"
+ "Crashing due to EINVAL"
+ "Crashing due to EIO"
+ "Crashing due to EISDIR"
+ "Crashing due to ELOOP"
+ "Crashing due to EMFILE"
+ "Crashing due to EMLINK"
+ "Crashing due to ENAMETOOLONG"
+ "Crashing due to ENFILE"
+ "Crashing due to ENOENT"
+ "Crashing due to ENOMEM"
+ "Crashing due to ENOSPC"
+ "Crashing due to ENOTDIR"
+ "Crashing due to EPERM"
+ "Crashing due to EROFS"
+ "Crashing due to ESPIPE"
+ "Crashing due to ETIMEDOUT"
+ "DEF"
+ "I"
+ "I16@0:8"
+ "IN"
+ "INV"
+ "MAINTENANCE"
+ "N"
+ "PFAbstractStateCaptureEvent"
+ "PFStateCaptureEvent"
+ "PFStateCaptureEventDescription"
+ "PFStateCaptureEventLog"
+ "T@\"NSArray\",R,C,N"
+ "T@\"NSString\",R"
+ "TI,V_qosClass"
+ "TQ,R,N"
+ "TQ,V_threadID"
+ "Td,R,N,V_startTimestamp"
+ "Td,V_endTimestamp"
+ "Td,V_startTimestamp"
+ "UN"
+ "UNKNOWN"
+ "UT"
+ "Y"
+ "_description"
+ "_endTimestamp"
+ "_eventClass"
+ "_lock_events"
+ "_lock_headIndex"
+ "_maxEvents"
+ "_qosClass"
+ "_startTimestamp"
+ "_threadID"
+ "addEvent"
+ "appendAbsoluteTimestamp:"
+ "appendBool:"
+ "appendDuration:"
+ "appendEndTimestamp:"
+ "appendFormat:"
+ "appendInteger:"
+ "appendQoSClass:"
+ "appendRelativeTimestamp:"
+ "appendString:"
+ "appendThreadID:"
+ "appendUInt64:"
+ "appendUnsignedInteger:"
+ "currentThreadID"
+ "end"
+ "endTimestamp"
+ "eventDescription"
+ "eventDescriptions"
+ "initWithEventClass:maxEvents:"
+ "initWithStartTimestamp:"
+ "objectAtIndexedSubscript:"
+ "qosClass"
+ "setEndTimestamp:"
+ "setInitialValues"
+ "setQosClass:"
+ "setStartTimestamp:"
+ "setThreadID:"
+ "startTimestamp"
+ "threadID"
+ "v20@0:8I16"
- "%{public}@: Removing state handler: %llu"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/Projects/PhotoFoundation/Source/PFAssert.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/Projects/PhotoFoundation/Source/PFGeometryUtilities.m"

```
