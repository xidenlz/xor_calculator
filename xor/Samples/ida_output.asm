int __fastcall main(int argc, const char **argv, const char **envp)
{
  __m128i si128; // xmm0
  char _Format[16]; // [rsp+20h] [rbp-28h] BYREF
  __m128i v6; // [rsp+30h] [rbp-18h]

  printf("first\n");
  *(_QWORD *)_Format = 0x5590329DB441A4BBLL;
  *(_QWORD *)&_Format[8] = 0xCBD43E3710EE1EF6uLL;
  v6.m128i_i64[0] = 0x3AC712F2D82DC1F3LL;
  si128 = _mm_load_si128((const __m128i *)_Format);
  v6.m128i_i64[1] = 0xCBD43E371A8A7284uLL;
  *(__m128i *)_Format = _mm_xor_si128(si128, v6);
  printf(_Format);
  return 0;
}