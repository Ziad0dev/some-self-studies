# Extensive Cryptography Study Guide: From Foundations to Real-World Systems

## Introduction

This guide is crafted for those wanting to learn everything about cryptography—from mathematical foundations to cutting-edge, real-world applications. Throughout, you’ll see references to Signal Protocol and Monero as practical, security-critical implementations.

---

## 1. Mathematical Foundations

### 1.1. Prerequisite Mathematics
- **Discrete Mathematics**  
  - Sets, relations, functions, logic, combinatorics, graphs, and trees.
  - Text: “Discrete Mathematics and Its Applications” by Kenneth H. Rosen.

- **Modular Arithmetic**  
  - Operations modulo n, congruences, Chinese Remainder Theorem, Euler’s theorem, Fermat’s little theorem.
  - Connection: Used in RSA, ElGamal, and Diffie-Hellman key exchange.

- **Number Theory**  
  - Prime numbers, GCD, LCM, factorization, Euler’s phi function, quadratic residues.
  - Text: “Elementary Number Theory” by David M. Burton.

- **Probability and Statistics**  
  - Random variables, distributions, entropy, collision probability, birthday paradox.
  - Application: Attack probabilities, hash collisions, PRNG analysis.

- **Algebra & Group Theory**  
  - Groups, rings, fields, cyclic groups, finite fields (Galois fields), vector spaces.
  - Application: Underlies elliptic curve cryptography (ECC), block ciphers, error-correcting codes.
  - Online: [MIT OpenCourseWare: Algebra I](https://ocw.mit.edu/courses/18-701-algebra-i-fall-2010/)

- **Elliptic Curves**  
  - EC group law, point addition, scalar multiplication, ECDLP (Elliptic Curve Discrete Log Problem).
  - Application: Curve25519 (used in Signal and Monero), EdDSA, ECDH.

- **Lattices (for Post-Quantum Crypto)**  
  - Lattice definitions, basis, Gram-Schmidt, shortest vector problem (SVP).
  - Application: Lattice-based cryptography (Kyber, Dilithium).

- **Information Theory**  
  - Entropy, mutual information, perfect secrecy (Shannon).
  - Application: OTP security, analysis of cryptosystems.

---

## 2. Complexity Theory

- **Hardness Assumptions**
  - One-way functions, trapdoor functions, computational vs. information-theoretic security.
- **P, NP, NP-hard, NP-complete problems**  
  - Reductions, probabilistic polynomial time, relation to cryptanalysis.
- Text: “Introduction to the Theory of Computation” by Michael Sipser.

---

## 3. Classical Cryptography

### 3.1. Historical Ciphers
- Caesar, Vigenère, Enigma, One-Time Pad (OTP)
- Mathematical underpinning: frequency analysis, modulo arithmetic (for ciphers like Caesar/Vigenère)
- Book: “The Code Book” by Simon Singh

### 3.2. Shannon’s Principles
- Confusion and diffusion (mathematical mixing of input bits)
- Perfect secrecy: H(M|C) = H(M)
- Article: [Shannon’s “Communication Theory of Secrecy Systems”](https://archive.org/details/bstj28-4-656)

---

## 4. Modern Cryptography

### 4.1. Cryptographic Primitives

#### 4.1.1. Symmetric Encryption
- **Block ciphers (AES, DES)**:  
  - Finite field (GF(2^8)) arithmetic, S-boxes (non-linear mappings), permutation matrices.
  - AES: mix columns (matrix multiplication in GF(2^8)), round keys.
- **Stream ciphers (RC4, ChaCha20)**:  
  - Linear algebra for state updates, modular addition, XOR.

#### 4.1.2. Asymmetric Encryption
- **RSA**:  
  - Modular exponentiation, Euler’s theorem, integer factorization problem.
- **Diffie-Hellman (DH)**:  
  - Discrete logarithm problem (DLP) in finite cyclic groups.
- **Elliptic Curve Cryptography (ECC)**:  
  - Elliptic curve group law:  
    y² = x³ + ax + b (mod p), point addition, scalar multiplication.
  - ECDLP: Hardness underpins security (Curve25519 in Signal and Monero).

#### 4.1.3. Hash Functions
- **SHA Family**:  
  - Bitwise operations, modular arithmetic, Merkle-Damgård construction, sponge construction (SHA-3/Keccak).
- **Birthday Paradox**:  
  - Probability theory for collision resistance.

#### 4.1.4. Digital Signatures
- **RSA, DSA, ECDSA, EdDSA**:  
  - Modular arithmetic, DLP/ECDLP, hash functions.

#### 4.1.5. Random Number Generation
- Algorithms based on entropy pools, statistical tests for randomness.
- Mathematical significance: uniformity, unpredictability.

---

### 4.2. Protocols & Constructions

#### 4.2.1. Key Exchange & Derivation
- DH and ECDH:  
  - Group theory, modular exponentiation, EC point multiplication.
- KDFs (HKDF in Signal):  
  - HMAC, entropy extraction, pseudo-randomness.

#### 4.2.2. Authenticated Encryption
- AEAD (AES-GCM, ChaCha20-Poly1305):  
  - Galois field multiplication, polynomial evaluation, nonce arithmetic.

#### 4.2.3. Commitment Schemes & Zero-Knowledge Proofs (ZKP)
- **Pedersen Commitment**:  
  - Group theory, modular arithmetic, hiding and binding properties.
- **Bulletproofs (Monero)**:  
  - Inner product arguments, vector commitment, elliptic curve operations.

#### 4.2.4. Secure Multiparty Computation (MPC)
- Secret sharing (Shamir):  
  - Polynomial interpolation over finite fields.

#### 4.2.5. Post-Quantum Cryptography
- **Lattice-based (Kyber, Dilithium)**:  
  - Lattice mathematics, ring learning with errors (Ring-LWE), module lattices.

---

## 5. Cryptographic Protocols in Practice

### 5.1. Signal Protocol
- **Double Ratchet**:  
  - Combines DH (asymmetric) and symmetric-key ratchets.
  - Math: EC Diffie-Hellman, KDF chains, forward secrecy via repeated key updates.
- **X3DH Key Agreement**:  
  - Multiple DH exchanges, EC math.
- **Noise Protocol**:  
  - Modular handshake patterns, DH, symmetric ciphers, hashes.
- **zkgroup/zkcredential**:  
  - Zero-knowledge proofs: group membership without revealing secrets.
- **Kyber (Post-quantum Signal)**:  
  - Lattice-based cryptography.

### 5.2. Monero
- **Ring Signatures**:  
  - Set theory, DLP, elliptic curves, anonymity set math.
- **Stealth Addresses**:  
  - EC math, Diffie-Hellman.
- **Bulletproofs**:  
  - Inner product proofs, vector and matrix algebra.
- **Tor/I2P**:  
  - Onion routing, graph theory, probability (cover traffic analysis).
- **Curve25519, EdDSA**:  
  - EC group law, modular arithmetic, hash-to-curve.

---

## 6. Advanced Topics

### 6.1. Lattice-Based and Post-Quantum Cryptography
- Lattice basis, Gram-Schmidt orthogonalization, SVP, LWE/Ring-LWE.

### 6.2. Homomorphic Encryption
- Ring and field operations, polynomial arithmetic.

### 6.3. Secure Hardware
- Side-channel countermeasures: constant-time algorithms (timing attack resistance), masking.

---

## 7. Further Reading and Problem Sets

### Books
- “Serious Cryptography” by Jean-Philippe Aumasson
- “Introduction to Modern Cryptography” by Katz & Lindell
- “Handbook of Applied Cryptography” by Menezes, van Oorschot, Vanstone (free online)

### Problem Sets and Courses
- [Stanford CS255: Cryptography](https://crypto.stanford.edu/~dabo/cs255/)
- [MIT 6.857: Network and Computer Security](https://ocw.mit.edu/courses/6-857-network-and-computer-security-spring-2014/)
- [Cryptopals Crypto Challenges](https://cryptopals.com/) — Highly recommended for practice!

---

## 8. Capstone: From Theory to Implementation

For every major topic above, attempt the following:
- Write out the underlying mathematical formulae and prove key properties (e.g., why ECDLP is hard, why Pedersen commitments are hiding and binding).
- Implement toy versions in your favorite programming language.
- Compare with and analyze the real implementations in Signal and Monero, noting how mathematical security translates to code and protocol decisions.

---

## 9. Reference List

- [Signal Protocol Docs](https://signal.org/docs/)
- [Monero Research Lab](https://www.getmonero.org/resources/research-lab/)
- [CryptoNote Whitepaper](https://cryptonote.org/whitepaper.pdf)
- [Handbook of Applied Cryptography (free)](https://cacr.uwaterloo.ca/hac/)
- [Awesome Cryptography](https://github.com/sobolevn/awesome-cryptography)

---

> **Pro-Tip:** As you encounter each cryptographic primitive or protocol, ask:
> - What are the mathematical problems it relies on?
> - What are the key equations or theorems?
> - How does the implementation in Signal or Monero realize these, and what trade-offs are involved?

Happy learning, and may your math be as strong as your code!