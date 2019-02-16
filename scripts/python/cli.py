#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import random
import time

import click
import pandas as pd
from faker import Faker

from utils import send_to_db


@click.group()
@click.option('--dry-run/--no-dry-run', default=False)
@click.pass_context
def cli(ctx, dry_run):
    if dry_run:
        click.echo('Running dry-run mode.')

    ctx.ensure_object(dict)
    ctx.obj['DRY_RUN'] = dry_run


@cli.command()
@click.option('--times', default=3, help='number of times to run')
@click.pass_context
def patient_data(ctx, times):
    click.echo('Sending patient data')
    fake = Faker()
    for _ in range(3):
        click.echo(click.style(
            f'Start generating fake data: {datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")}',
            fg='green'
        ))
        # fake patient data
        patient_data = []
        # populate 100.000 records of fake data
        for _ in range(100000):
            patient_data.append({
                'Name': fake.name(),
                'PhoneNumber': fake.phone_number(),
                'Address': fake.address(),
                'City': fake.city(),
                'BirthDate': fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=90),
                'Height': random.randint(150, 200),
                'Weight': random.randint(45, 120),
            })
        # convert to a data frame
        patient_df = pd.DataFrame(patient_data)
        # reassign index value to start from 1
        patient_df.index = range(1, len(patient_df) + 1)
        click.echo(click.style(
            f'Finished generating fake data: {datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")}',
            fg='green'
        ))
        if not ctx.obj['DRY_RUN']:
            send_to_db(patient_df, index_label='Id')
            click.echo(click.style(
                'Database import done',
                fg='green'
            ))

        click.echo(click.style(
            'Waiting for 1 minute ...',
            fg='cyan'
        ))
        time.sleep(60)


@cli.command()
@click.option('--times', default=3, help='number of times to run')
@click.pass_context
def healthcare_sensor(ctx, times):
    click.echo('Sending healthcare data')
    for _ in range(3):
        click.echo(click.style(
            f'Start generating fake data: {datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")}',
            fg='green'
        ))

        # create a dictionary to hold the fake data
        healthcare_data = []
        # Populate the dictionary with 100.000 records of fake data
        for _ in range(100000):
            healthcare_data.append({
                'time': datetime.datetime.now(),
                'SystolicBloodPressure': random.randint(90, 190),
                'DiastolicBloodPressure': random.randint(40, 140),
                'HeartRate': random.randint(50, 250)
            })

        # convert to a data frame
        healthcare_df = pd.DataFrame(healthcare_data)
        # reset the index - it should be always between 1 and 100.000 as this is the PatientId
        healthcare_df.reset_index(drop=True)
        # Reassign the index value to start from 1
        healthcare_df.index = range(1, len(healthcare_df) + 1)
        click.echo(click.style(
            f'Finished generating fake data: {datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")}',
            fg='green'
        ))
        if not ctx.obj['DRY_RUN']:
            send_to_db(healthcare_df, index_label='PatientId')
            click.echo(click.style(
                'Database import done',
                fg='green'
            ))

        click.echo(click.style(
            'Waiting for 1 minute ...',
            fg='cyan'
        ))
        time.sleep(60)

if __name__ == '__main__':
    cli(obj={})
