## oncrpc

> `/System/Library/PrivateFrameworks/oncrpc.framework/Versions/A/oncrpc`

```diff

-  __TEXT.__text: 0x13550
+  __TEXT.__text: 0x13584
   __TEXT.__const: 0xe0
   __TEXT.__oslogstring: 0x487
   __TEXT.__cstring: 0x1da6
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ __newrpclib_netid2socparms : 240 -> 220
~ _clnt_sperror_r : 572 -> 588
~ __newrpclib_clnt_sperrno : 68 -> 76
~ __newrpclib_clnt_perrno : 80 -> 88
~ __newrpclib_clnt_spcreateerror : 428 -> 444
~ _ugetport : 256 -> 272
~ _getnetconfigent : 200 -> 208
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/auth_none.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/auth_unix.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/clnt_perror.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/clnt_raw.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/clnt_strm.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/rpc_control.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/rpc_inet.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/rpcbind.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/svc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/svc_auth.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/svc_run.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/svc_simple.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/svc_strm.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/svc_udp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/svc_xprt.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/xdr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/xdr_array.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/xdr_rec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FKFa5g/Sources/oncrpc/Oncrpc/xdr_reference.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/auth_none.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/auth_unix.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/clnt_perror.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/clnt_raw.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/clnt_strm.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/rpc_control.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/rpc_inet.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/rpcbind.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/svc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/svc_auth.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/svc_run.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/svc_simple.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/svc_strm.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/svc_udp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/svc_xprt.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/xdr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/xdr_array.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/xdr_rec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uCG7nO/Sources/oncrpc/Oncrpc/xdr_reference.c"

```
