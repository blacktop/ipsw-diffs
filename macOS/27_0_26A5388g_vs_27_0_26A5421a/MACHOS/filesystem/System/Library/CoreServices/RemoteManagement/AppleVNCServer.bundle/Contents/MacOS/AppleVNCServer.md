## AppleVNCServer

> `/System/Library/CoreServices/RemoteManagement/AppleVNCServer.bundle/Contents/MacOS/AppleVNCServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-756.34.0.0.0
-  __TEXT.__text: 0x844f8
-  __TEXT.__auth_stubs: 0x2620
+756.36.5.2.0
+  __TEXT.__text: 0x86be0
+  __TEXT.__auth_stubs: 0x2630
   __TEXT.__objc_stubs: 0x34a0
   __TEXT.__objc_methlist: 0x1490
-  __TEXT.__cstring: 0x1faab
-  __TEXT.__oslogstring: 0xe615
-  __TEXT.__const: 0x208a
-  __TEXT.__objc_methname: 0x45af
+  __TEXT.__cstring: 0x2032f
+  __TEXT.__oslogstring: 0xebf3
+  __TEXT.__const: 0x2092
+  __TEXT.__objc_methname: 0x45b4
   __TEXT.__objc_classname: 0x203
-  __TEXT.__objc_methtype: 0x2a57
+  __TEXT.__objc_methtype: 0x2a6b
   __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__unwind_info: 0xae0
-  __DATA_CONST.__const: 0xbc0
+  __TEXT.__unwind_info: 0xb40
+  __DATA_CONST.__const: 0xe90
   __DATA_CONST.__cfstring: 0x1780
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x1320
+  __DATA_CONST.__auth_got: 0x1328
   __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0x1a90

   __DATA.__objc_ivar: 0xfc
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x3668
-  __DATA.__bss: 0xbfc
+  __DATA.__bss: 0xcec
   __DATA.__common: 0x6cc1
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1264
-  Symbols:   768
-  CStrings:  3768
+  Functions: 1305
+  Symbols:   769
+  CStrings:  3816
 
Symbols:
+ _CGEventPostToPid
+ _dispatch_after
- _objc_opt_respondsToSelector
CStrings:
+ "ApplyPendingCancelOnDragQueue"
+ "Applying deferred cancel (%s)"
+ "CGEventCreate returned NULL"
+ "CreateSyntheticMouseMovementsOnDragQueue"
+ "Deferred synthetic mouse-down at %.1f %.1f"
+ "Deferring cancel (SSDragHelper not in drag loop yet)"
+ "Drag wake-up: posted 2-px nudge at %.1f,%.1f and back, to wake CoreDrag's drag loop"
+ "FlushPendingMouseUpOnDragQueue"
+ "FlushPendingMouseUpOnDragQueue (%s): nothing buffered, skipping"
+ "FlushSyntheticDownOnDragQueue"
+ "Flushing buffered mouse-up at %.1f,%.1f (%s)"
+ "OpenDragHelperApp_block_invoke"
+ "Posted LeftMouseDragged directly to helper  pid %d at (%d,%d) pt (bypass cursor-zone routing)"
+ "Posting deferred synthetic mouse-down at %.1f,%.1f (%s)"
+ "Refuse to run file receiver as uid %u"
+ "Refuse to run file sender as uid %u"
+ "SaveAdvertisedAuthTypes"
+ "ScrapConnectionArmMouseUpGate_block_invoke"
+ "ScrapConnectionBufferMouseUpIfNeeded"
+ "ScrapConnectionBufferMouseUpIfNeeded: mask=0x%x has bit 0 set, not a mouse-up; not buffering at %.1f,%.1f"
+ "ScrapConnectionBufferMouseUpIfNeeded: pos=%.1f,%.1f mask=0x%x → buffered=%d (%s)"
+ "ScrapConnectionBufferMouseUpIfNeeded_block_invoke"
+ "ScrapConnectionFinishInitialization"
+ "ScrapConnectionResetDragGate_block_invoke"
+ "Skip deferred synthetic mouse-down — drag ended (%s)"
+ "T^{?=i^{?}IICCSISCCCICII{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{?=CCCCSSSCCCCCC}CCCC{Point=ss}{Point=ss}IIIIICCCCCCCCCCCCCCCCCCCCii[4{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}][4i][4i]{UserInfoEncoding=CC{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}[4{SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}]^?*S[16C]^{?}^{?}^{?}^{?}@^{?}^v^v^v^{_opaque_pthread_t}^vIiCCCCd*ISSSSSssS^{CGContext}^{CGColorSpace}^vI^{ARDBigNum}^{ARDBigNum}^{ARDBigNum}SCCI^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}ICCCCCCCCCCCC^{?}IISCCICCCC*III*IIICCS{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}IS[16C][512C]^v^{ScreenChangeInfo}^{ScreenChangeInfo}{UnsignedWide=II}IICCCIS[16C][16C]CC[16C][16C]II**^{__CFString}{MVSInfo=SSSSISs{Rect=ssss}CC{Rect=ssss}{Rect=ssss}CC[2c]I{Point=ss}S**^vC^{MVSCoefficeintInfo}{?=^{MVSCacheEntryInfo}SSI^SIIIIi}}^{?}^{CachedCursor}*I{Rect=ssss}^{RFBSenderInfoUDP}^{RFBReceiverInfoUDP}{ZRLEInfo={SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}*II}[25{ScaledScreenInfo=^{_CGLContextObject}^{_CGLPixelFormatObject}^{_CGLPBufferObject}^{CGColorSpace}}]CCCCI{ViewerInfo=iIIIIIII[32C]}ICCCCI^{FileCopy_Globals}IIIIBCCCCCSCC^{UnixToolSessionInfo}^v*^{?}^vB@^{__CFRunLoopTimer}{ViewerMouseInfo={CGPoint=dd}ISQI}{Rect=ssss}CCCCI[25I][25{Rect=ssss}]{Point=ss}QCCIi{kevent=QsSIq^v}I^{srp_context}CCCCCQ^v*I***CCCCiSC[51C]CCCCCCS[2C]CCCCCCCI@CCC^v[64c]IC},V_viewer"
+ "Unable to create CGEvent"
+ "Using buffered drop pos %.0f,%.0f (captured was %.1f,%.1f)"
+ "^{?=i^{?}IICCSISCCCICII{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{?=CCCCSSSCCCCCC}CCCC{Point=ss}{Point=ss}IIIIICCCCCCCCCCCCCCCCCCCCii[4{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}][4i][4i]{UserInfoEncoding=CC{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}[4{SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}]^?*S[16C]^{?}^{?}^{?}^{?}@^{?}^v^v^v^{_opaque_pthread_t}^vIiCCCCd*ISSSSSssS^{CGContext}^{CGColorSpace}^vI^{ARDBigNum}^{ARDBigNum}^{ARDBigNum}SCCI^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}ICCCCCCCCCCCC^{?}IISCCICCCC*III*IIICCS{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}IS[16C][512C]^v^{ScreenChangeInfo}^{ScreenChangeInfo}{UnsignedWide=II}IICCCIS[16C][16C]CC[16C][16C]II**^{__CFString}{MVSInfo=SSSSISs{Rect=ssss}CC{Rect=ssss}{Rect=ssss}CC[2c]I{Point=ss}S**^vC^{MVSCoefficeintInfo}{?=^{MVSCacheEntryInfo}SSI^SIIIIi}}^{?}^{CachedCursor}*I{Rect=ssss}^{RFBSenderInfoUDP}^{RFBReceiverInfoUDP}{ZRLEInfo={SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}*II}[25{ScaledScreenInfo=^{_CGLContextObject}^{_CGLPixelFormatObject}^{_CGLPBufferObject}^{CGColorSpace}}]CCCCI{ViewerInfo=iIIIIIII[32C]}ICCCCI^{FileCopy_Globals}IIIIBCCCCCSCC^{UnixToolSessionInfo}^v*^{?}^vB@^{__CFRunLoopTimer}{ViewerMouseInfo={CGPoint=dd}ISQI}{Rect=ssss}CCCCI[25I][25{Rect=ssss}]{Point=ss}QCCIi{kevent=QsSIq^v}I^{srp_context}CCCCCQ^v*I***CCCCiSC[51C]CCCCCCS[2C]CCCCCCCI@CCC^v[64c]IC}"
+ "^{?=i^{?}IICCSISCCCICII{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{?=CCCCSSSCCCCCC}CCCC{Point=ss}{Point=ss}IIIIICCCCCCCCCCCCCCCCCCCCii[4{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}][4i][4i]{UserInfoEncoding=CC{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}[4{SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}]^?*S[16C]^{?}^{?}^{?}^{?}@^{?}^v^v^v^{_opaque_pthread_t}^vIiCCCCd*ISSSSSssS^{CGContext}^{CGColorSpace}^vI^{ARDBigNum}^{ARDBigNum}^{ARDBigNum}SCCI^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}ICCCCCCCCCCCC^{?}IISCCICCCC*III*IIICCS{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}IS[16C][512C]^v^{ScreenChangeInfo}^{ScreenChangeInfo}{UnsignedWide=II}IICCCIS[16C][16C]CC[16C][16C]II**^{__CFString}{MVSInfo=SSSSISs{Rect=ssss}CC{Rect=ssss}{Rect=ssss}CC[2c]I{Point=ss}S**^vC^{MVSCoefficeintInfo}{?=^{MVSCacheEntryInfo}SSI^SIIIIi}}^{?}^{CachedCursor}*I{Rect=ssss}^{RFBSenderInfoUDP}^{RFBReceiverInfoUDP}{ZRLEInfo={SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}*II}[25{ScaledScreenInfo=^{_CGLContextObject}^{_CGLPixelFormatObject}^{_CGLPBufferObject}^{CGColorSpace}}]CCCCI{ViewerInfo=iIIIIIII[32C]}ICCCCI^{FileCopy_Globals}IIIIBCCCCCSCC^{UnixToolSessionInfo}^v*^{?}^vB@^{__CFRunLoopTimer}{ViewerMouseInfo={CGPoint=dd}ISQI}{Rect=ssss}CCCCI[25I][25{Rect=ssss}]{Point=ss}QCCIi{kevent=QsSIq^v}I^{srp_context}CCCCCQ^v*I***CCCCiSC[51C]CCCCCCS[2C]CCCCCCCI@CCC^v[64c]IC}16@0:8"
+ "already buffered (gPendingMouseUp.valid=TRUE) — keeping earlier event"
+ "bad auth type list - length %u count %u"
+ "buffered new entry"
+ "buffering mouse-up at %.1f,%.1f (mask=0x%x)"
+ "cancel safety timeout"
+ "cancel safety timeout elapsed"
+ "com.apple.applevncserver.dragQueue"
+ "gate already ready (gDragHelperReadyForMouseUp=TRUE)"
+ "gate armed: gDragInFlight=TRUE, gDragHelperReadyForMouseUp=FALSE, token=%llu"
+ "gate not armed (gDragInFlight=FALSE)"
+ "gate reset: gDragInFlight=FALSE, gDragHelperReadyForMouseUp=FALSE"
+ "gate safety timeout fired: gDragHelperReadyForMouseUp=TRUE"
+ "helper EventLoopReady"
+ "helper entered receiver"
+ "kRFBDragHelperEnteredReceiver"
+ "kRFBDragHelperEventLoopReady"
+ "motion pump tick %d: Dragged -> helper pid %d at (%.0f,%.0f) pt"
+ "motion pump: backstop deadline reached (%d ticks); stopping"
+ "mouse mask %x"
+ "reset (drag ended)"
+ "safety timeout"
+ "v24@0:8^{?=i^{?}IICCSISCCCICII{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{?=CCCCSSSCCCCCC}CCCC{Point=ss}{Point=ss}IIIIICCCCCCCCCCCCCCCCCCCCii[4{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}][4i][4i]{UserInfoEncoding=CC{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}[4{SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}]^?*S[16C]^{?}^{?}^{?}^{?}@^{?}^v^v^v^{_opaque_pthread_t}^vIiCCCCd*ISSSSSssS^{CGContext}^{CGColorSpace}^vI^{ARDBigNum}^{ARDBigNum}^{ARDBigNum}SCCI^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}ICCCCCCCCCCCC^{?}IISCCICCCC*III*IIICCS{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}IS[16C][512C]^v^{ScreenChangeInfo}^{ScreenChangeInfo}{UnsignedWide=II}IICCCIS[16C][16C]CC[16C][16C]II**^{__CFString}{MVSInfo=SSSSISs{Rect=ssss}CC{Rect=ssss}{Rect=ssss}CC[2c]I{Point=ss}S**^vC^{MVSCoefficeintInfo}{?=^{MVSCacheEntryInfo}SSI^SIIIIi}}^{?}^{CachedCursor}*I{Rect=ssss}^{RFBSenderInfoUDP}^{RFBReceiverInfoUDP}{ZRLEInfo={SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}*II}[25{ScaledScreenInfo=^{_CGLContextObject}^{_CGLPixelFormatObject}^{_CGLPBufferObject}^{CGColorSpace}}]CCCCI{ViewerInfo=iIIIIIII[32C]}ICCCCI^{FileCopy_Globals}IIIIBCCCCCSCC^{UnixToolSessionInfo}^v*^{?}^vB@^{__CFRunLoopTimer}{ViewerMouseInfo={CGPoint=dd}ISQI}{Rect=ssss}CCCCI[25I][25{Rect=ssss}]{Point=ss}QCCIi{kevent=QsSIq^v}I^{srp_context}CCCCCQ^v*I***CCCCiSC[51C]CCCCCCS[2C]CCCCCCCI@CCC^v[64c]IC}16"
+ "v28@0:8i16^{?=i^{?}IICCSISCCCICII{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{?=CCCCSSSCCCCCC}CCCC{Point=ss}{Point=ss}IIIIICCCCCCCCCCCCCCCCCCCCii[4{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}][4i][4i]{UserInfoEncoding=CC{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}[4{SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}]^?*S[16C]^{?}^{?}^{?}^{?}@^{?}^v^v^v^{_opaque_pthread_t}^vIiCCCCd*ISSSSSssS^{CGContext}^{CGColorSpace}^vI^{ARDBigNum}^{ARDBigNum}^{ARDBigNum}SCCI^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}ICCCCCCCCCCCC^{?}IISCCICCCC*III*IIICCS{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}IS[16C][512C]^v^{ScreenChangeInfo}^{ScreenChangeInfo}{UnsignedWide=II}IICCCIS[16C][16C]CC[16C][16C]II**^{__CFString}{MVSInfo=SSSSISs{Rect=ssss}CC{Rect=ssss}{Rect=ssss}CC[2c]I{Point=ss}S**^vC^{MVSCoefficeintInfo}{?=^{MVSCacheEntryInfo}SSI^SIIIIi}}^{?}^{CachedCursor}*I{Rect=ssss}^{RFBSenderInfoUDP}^{RFBReceiverInfoUDP}{ZRLEInfo={SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}*II}[25{ScaledScreenInfo=^{_CGLContextObject}^{_CGLPixelFormatObject}^{_CGLPBufferObject}^{CGColorSpace}}]CCCCI{ViewerInfo=iIIIIIII[32C]}ICCCCI^{FileCopy_Globals}IIIIBCCCCCSCC^{UnixToolSessionInfo}^v*^{?}^vB@^{__CFRunLoopTimer}{ViewerMouseInfo={CGPoint=dd}ISQI}{Rect=ssss}CCCCI[25I][25{Rect=ssss}]{Point=ss}QCCIi{kevent=QsSIq^v}I^{srp_context}CCCCCQ^v*I***CCCCiSC[51C]CCCCCCS[2C]CCCCCCCI@CCC^v[64c]IC}20"
+ "viewer requested RSA SRP but SRP was not advertised"
+ "viewer selected auth type %u which was not advertised"
- "ScrapConnectionFinishInitilization"
- "T^{?=i^{?}IICCSISCCCICII{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{?=CCCCSSSCCCCCC}CCCC{Point=ss}{Point=ss}IIIIICCCCCCCCCCCCCCCCCCCCii[4{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}][4i][4i]{UserInfoEncoding=CC{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}[4{SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}]^?*S[16C]^{?}^{?}^{?}^{?}@^{?}^v^v^v^{_opaque_pthread_t}^vIiCCCCd*ISSSSSssS^{CGContext}^{CGColorSpace}^vI^{ARDBigNum}^{ARDBigNum}^{ARDBigNum}SCCI^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}ICCCCCCCCCCCC^{?}IISCCICCCC*III*IIICCS{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}IS[16C][512C]^v^{ScreenChangeInfo}^{ScreenChangeInfo}{UnsignedWide=II}IICCCIS[16C][16C]CC[16C][16C]II**^{__CFString}{MVSInfo=SSSSISs{Rect=ssss}CC{Rect=ssss}{Rect=ssss}CC[2c]I{Point=ss}S**^vC^{MVSCoefficeintInfo}{?=^{MVSCacheEntryInfo}SSI^SIIIIi}}^{?}^{CachedCursor}*I{Rect=ssss}^{RFBSenderInfoUDP}^{RFBReceiverInfoUDP}{ZRLEInfo={SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}*II}[25{ScaledScreenInfo=^{_CGLContextObject}^{_CGLPixelFormatObject}^{_CGLPBufferObject}^{CGColorSpace}}]CCCCI{ViewerInfo=iIIIIIII[32C]}ICCCCI^{FileCopy_Globals}IIIIBCCCCCSCC^{UnixToolSessionInfo}^v*^{?}^vB@^{__CFRunLoopTimer}{ViewerMouseInfo={CGPoint=dd}ISQI}{Rect=ssss}CCCCI[25I][25{Rect=ssss}]{Point=ss}QCCIi{kevent=QsSIq^v}I^{srp_context}CCCCCQ^v*I***CCCCiSCCCCCCCS[2C]CCCCCCCI@CCC^v[64c]IC},V_viewer"
- "^{?=i^{?}IICCSISCCCICII{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{?=CCCCSSSCCCCCC}CCCC{Point=ss}{Point=ss}IIIIICCCCCCCCCCCCCCCCCCCCii[4{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}][4i][4i]{UserInfoEncoding=CC{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}[4{SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}]^?*S[16C]^{?}^{?}^{?}^{?}@^{?}^v^v^v^{_opaque_pthread_t}^vIiCCCCd*ISSSSSssS^{CGContext}^{CGColorSpace}^vI^{ARDBigNum}^{ARDBigNum}^{ARDBigNum}SCCI^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}ICCCCCCCCCCCC^{?}IISCCICCCC*III*IIICCS{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}IS[16C][512C]^v^{ScreenChangeInfo}^{ScreenChangeInfo}{UnsignedWide=II}IICCCIS[16C][16C]CC[16C][16C]II**^{__CFString}{MVSInfo=SSSSISs{Rect=ssss}CC{Rect=ssss}{Rect=ssss}CC[2c]I{Point=ss}S**^vC^{MVSCoefficeintInfo}{?=^{MVSCacheEntryInfo}SSI^SIIIIi}}^{?}^{CachedCursor}*I{Rect=ssss}^{RFBSenderInfoUDP}^{RFBReceiverInfoUDP}{ZRLEInfo={SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}*II}[25{ScaledScreenInfo=^{_CGLContextObject}^{_CGLPixelFormatObject}^{_CGLPBufferObject}^{CGColorSpace}}]CCCCI{ViewerInfo=iIIIIIII[32C]}ICCCCI^{FileCopy_Globals}IIIIBCCCCCSCC^{UnixToolSessionInfo}^v*^{?}^vB@^{__CFRunLoopTimer}{ViewerMouseInfo={CGPoint=dd}ISQI}{Rect=ssss}CCCCI[25I][25{Rect=ssss}]{Point=ss}QCCIi{kevent=QsSIq^v}I^{srp_context}CCCCCQ^v*I***CCCCiSCCCCCCCS[2C]CCCCCCCI@CCC^v[64c]IC}"
- "^{?=i^{?}IICCSISCCCICII{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{?=CCCCSSSCCCCCC}CCCC{Point=ss}{Point=ss}IIIIICCCCCCCCCCCCCCCCCCCCii[4{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}][4i][4i]{UserInfoEncoding=CC{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}[4{SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}]^?*S[16C]^{?}^{?}^{?}^{?}@^{?}^v^v^v^{_opaque_pthread_t}^vIiCCCCd*ISSSSSssS^{CGContext}^{CGColorSpace}^vI^{ARDBigNum}^{ARDBigNum}^{ARDBigNum}SCCI^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}ICCCCCCCCCCCC^{?}IISCCICCCC*III*IIICCS{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}IS[16C][512C]^v^{ScreenChangeInfo}^{ScreenChangeInfo}{UnsignedWide=II}IICCCIS[16C][16C]CC[16C][16C]II**^{__CFString}{MVSInfo=SSSSISs{Rect=ssss}CC{Rect=ssss}{Rect=ssss}CC[2c]I{Point=ss}S**^vC^{MVSCoefficeintInfo}{?=^{MVSCacheEntryInfo}SSI^SIIIIi}}^{?}^{CachedCursor}*I{Rect=ssss}^{RFBSenderInfoUDP}^{RFBReceiverInfoUDP}{ZRLEInfo={SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}*II}[25{ScaledScreenInfo=^{_CGLContextObject}^{_CGLPixelFormatObject}^{_CGLPBufferObject}^{CGColorSpace}}]CCCCI{ViewerInfo=iIIIIIII[32C]}ICCCCI^{FileCopy_Globals}IIIIBCCCCCSCC^{UnixToolSessionInfo}^v*^{?}^vB@^{__CFRunLoopTimer}{ViewerMouseInfo={CGPoint=dd}ISQI}{Rect=ssss}CCCCI[25I][25{Rect=ssss}]{Point=ss}QCCIi{kevent=QsSIq^v}I^{srp_context}CCCCCQ^v*I***CCCCiSCCCCCCCS[2C]CCCCCCCI@CCC^v[64c]IC}16@0:8"
- "posted at %d %d"
- "v24@0:8^{?=i^{?}IICCSISCCCICII{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{?=CCCCSSSCCCCCC}CCCC{Point=ss}{Point=ss}IIIIICCCCCCCCCCCCCCCCCCCCii[4{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}][4i][4i]{UserInfoEncoding=CC{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}[4{SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}]^?*S[16C]^{?}^{?}^{?}^{?}@^{?}^v^v^v^{_opaque_pthread_t}^vIiCCCCd*ISSSSSssS^{CGContext}^{CGColorSpace}^vI^{ARDBigNum}^{ARDBigNum}^{ARDBigNum}SCCI^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}ICCCCCCCCCCCC^{?}IISCCICCCC*III*IIICCS{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}IS[16C][512C]^v^{ScreenChangeInfo}^{ScreenChangeInfo}{UnsignedWide=II}IICCCIS[16C][16C]CC[16C][16C]II**^{__CFString}{MVSInfo=SSSSISs{Rect=ssss}CC{Rect=ssss}{Rect=ssss}CC[2c]I{Point=ss}S**^vC^{MVSCoefficeintInfo}{?=^{MVSCacheEntryInfo}SSI^SIIIIi}}^{?}^{CachedCursor}*I{Rect=ssss}^{RFBSenderInfoUDP}^{RFBReceiverInfoUDP}{ZRLEInfo={SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}*II}[25{ScaledScreenInfo=^{_CGLContextObject}^{_CGLPixelFormatObject}^{_CGLPBufferObject}^{CGColorSpace}}]CCCCI{ViewerInfo=iIIIIIII[32C]}ICCCCI^{FileCopy_Globals}IIIIBCCCCCSCC^{UnixToolSessionInfo}^v*^{?}^vB@^{__CFRunLoopTimer}{ViewerMouseInfo={CGPoint=dd}ISQI}{Rect=ssss}CCCCI[25I][25{Rect=ssss}]{Point=ss}QCCIi{kevent=QsSIq^v}I^{srp_context}CCCCCQ^v*I***CCCCiSCCCCCCCS[2C]CCCCCCCI@CCC^v[64c]IC}16"
- "v28@0:8i16^{?=i^{?}IICCSISCCCICII{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{Rect=ssss}{?=CCCCSSSCCCCCC}CCCC{Point=ss}{Point=ss}IIIIICCCCCCCCCCCCCCCCCCCCii[4{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}][4i][4i]{UserInfoEncoding=CC{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}[4{SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}]^?*S[16C]^{?}^{?}^{?}^{?}@^{?}^v^v^v^{_opaque_pthread_t}^vIiCCCCd*ISSSSSssS^{CGContext}^{CGColorSpace}^vI^{ARDBigNum}^{ARDBigNum}^{ARDBigNum}SCCI^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}^{_CCCryptor}ICCCCCCCCCCCC^{?}IISCCICCCC*III*IIICCS{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}IS[16C][512C]^v^{ScreenChangeInfo}^{ScreenChangeInfo}{UnsignedWide=II}IICCCIS[16C][16C]CC[16C][16C]II**^{__CFString}{MVSInfo=SSSSISs{Rect=ssss}CC{Rect=ssss}{Rect=ssss}CC[2c]I{Point=ss}S**^vC^{MVSCoefficeintInfo}{?=^{MVSCacheEntryInfo}SSI^SIIIIi}}^{?}^{CachedCursor}*I{Rect=ssss}^{RFBSenderInfoUDP}^{RFBReceiverInfoUDP}{ZRLEInfo={SubZlibCodecInfo=Cc{z_stream_s=*IQ*IQ*^{internal_state}^?^?^viQQ}}*II}[25{ScaledScreenInfo=^{_CGLContextObject}^{_CGLPixelFormatObject}^{_CGLPBufferObject}^{CGColorSpace}}]CCCCI{ViewerInfo=iIIIIIII[32C]}ICCCCI^{FileCopy_Globals}IIIIBCCCCCSCC^{UnixToolSessionInfo}^v*^{?}^vB@^{__CFRunLoopTimer}{ViewerMouseInfo={CGPoint=dd}ISQI}{Rect=ssss}CCCCI[25I][25{Rect=ssss}]{Point=ss}QCCIi{kevent=QsSIq^v}I^{srp_context}CCCCCQ^v*I***CCCCiSCCCCCCCS[2C]CCCCCCCI@CCC^v[64c]IC}20"
```
