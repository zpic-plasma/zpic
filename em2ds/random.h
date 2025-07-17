/*
 *  random.h
 *  zpic
 *
 *  Created by Ricardo Fonseca on 11/8/10.
 *  Copyright 2010 Centro de Física dos Plasmas. All rights reserved.
 *
 */

#ifndef __RANDOM__
#define __RANDOM__

#include <stdint.h>

/**
 * @brief Sets the seed for the pseudo random number generator
 * 
 * @param m_w_ Seed value w (must not be zero)
 * @param m_z_ Seed value z (must not be zero)
 */
void set_rand_seed( uint32_t m_w_, uint32_t m_z_ );

/**
 * @brief Returns the current seed for the pseudo random number generator
 * 
 * @param m_w_ Pointer to seed value w
 * @param m_z_ Pointer to seed value z
 */
void get_rand_seed( uint32_t* m_w_, uint32_t* m_z_ );

/**
 * @brief Returns a 32 bit pseudo random number using Marsaglia MWC algorithm
 * 
 * @return Random value in the range [0,2^32 - 1]
 */
uint32_t rand_uint32( void );

/**
 * @brief Returns a variate of the normal distribution (mean 0, stdev 1)
 * 
 * @return Double precision random number following a normal distribution 
 */
double rand_norm( void );

#endif
